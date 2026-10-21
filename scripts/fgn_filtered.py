"""E2: FGN surrogate matched after filtering.

The pipeline's FGN surrogate (FGN1) is tuned on the unfiltered rank sequence (length N) and
then filtered; scripts/filtered_rank_dfa.py shows that the filter lowers its rank-level DFA
exponent more than the original's.  Here a second surrogate (FGN2) is built directly on the
M tokens of the embedding trajectory (frequency filter and OOV removal already applied), with
alpha0 tuned by bisection so that the DFA exponent of its rank sequence matches that of the
original trajectory tokens, with the same estimator.  FGN2 is a permutation of the trajectory
tokens, so it shares the covariance, PCA eigensystem and projected marginals of the original;
it is projected on the original axes and compared with the original, the word-shuffled null
and FGN1 on the burstiness spectrum (all q), the projection ACF and the projection DFA.

Usage:
    python scripts/fgn_filtered.py data/corpus_v2 --manifest data/corpus_v2/manifest.csv \\
        --out results_v2/fgn_filtered
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, ttest_rel

from semburst.acf import acf_matrix, ci95
from semburst.burst import burstiness_spectrum, shuffled_burstiness, thresholds
from semburst.config import DEFAULT as P
from semburst.dfa import DFA_L_MIN, DFA_N_SCALES, dfa_exponent, projection_alpha, rank_l_max, zipf_table
from semburst.embed import build_trajectory, load_vectors
from semburst.pca import project
from semburst.pipeline import analyse_text
from semburst.surrogates import fgn_surrogate

LOW, HIGH = 0.55, 1.0     # bisection range for alpha0 (pipeline default: 0.55 .. 0.92)
LAGS = (1, 10, 100)


def rank_alpha(tokens, rank_of) -> float:
    """DFA exponent of the rank sequence, estimator of the FGN-matching step, with a given rank table."""
    r = np.array([rank_of[t] for t in tokens], dtype=np.float64)
    return dfa_exponent(r, DFA_L_MIN, rank_l_max(len(r)), DFA_N_SCALES)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus_dir")
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--out", default="results_v2/fgn_filtered")
    ap.add_argument("--texts", nargs="*")
    args = ap.parse_args()
    files = sorted(Path(args.corpus_dir) / f for f in args.texts) if args.texts else sorted(Path(args.corpus_dir).glob("*.txt"))
    genre = pd.read_csv(args.manifest).set_index("file").genre if args.manifest else None
    wv = load_vectors()
    key = wv.key_to_index

    rows, qrows, krows = [], [], []
    for f in files:
        a = analyse_text(f, wv)
        traj_tokens = [t for t in a.text.tokens_filtered if t in key]
        assert len(traj_tokens) == a.M
        # one rank table for all three sequences: that of the original trajectory tokens
        rank_of = {w: r for r, (w, _) in enumerate(zipf_table(traj_tokens), start=1)}
        fgn1_traj = [t for t in a.fgn.tokens if t not in a.text.stopset and a.text.freq[t] >= P.min_freq and t in key]
        fgn2 = fgn_surrogate(traj_tokens, seed=P.fgn_seed, low=LOW, high=HIGH)
        v2, _ = build_trajectory(fgn2.tokens, wv)
        assert len(v2) == a.M
        proj2 = project(v2, a.pca)
        assert np.array_equal(np.sort(proj2, 0), np.sort(a.pca.proj, 0)), "FGN2 marginals differ"

        series = {"orig": a.pca.proj, "fgn1": a.proj_fgn, "fgn2": proj2}
        r = {"file": f.name, "genre": genre.get(f.name, "") if genre is not None else "", "M": a.M,
             "alpha_traj_orig": fgn2.alpha_text, "alpha_traj_fgn1": rank_alpha(fgn1_traj, rank_of),
             "alpha_traj_fgn2": fgn2.alpha_surr, "alpha0_fgn1": a.fgn.alpha0, "alpha0_fgn2": fgn2.alpha0,
             "seed_fgn2": fgn2.seed, "bisect_evals_fgn2": len(fgn2.log)}
        for q in P.q_sweep:
            th = thresholds(a.pca.proj, q)
            b = {k: burstiness_spectrum(x, th) for k, x in series.items()}
            bs, _ = shuffled_burstiness(a.pca.proj, a.perms, th)
            qrows.append({"file": f.name, "q": q,
                          "orig_surr": (b["orig"] / bs).mean(), "fgn1_surr": (b["fgn1"] / bs).mean(),
                          "fgn2_surr": (b["fgn2"] / bs).mean(),
                          "order_fgn1": int(((b["orig"] > b["fgn1"]) & (b["orig"] > bs)).sum()),
                          "order_fgn2": int(((b["orig"] > b["fgn2"]) & (b["orig"] > bs)).sum())})
            if q == P.quantile:
                for j in range(P.k_burst):
                    krows.append({"file": f.name, "k": j + 1, "B_orig": b["orig"][j], "B_surr": bs[j],
                                  "B_fgn1": b["fgn1"][j], "B_fgn2": b["fgn2"][j]})
                r.update({k: qrows[-1][k] for k in ("orig_surr", "fgn1_surr", "fgn2_surr", "order_fgn1", "order_fgn2")})
                r["n_fgn2_within5"] = int((np.abs(b["fgn2"] / bs - 1) < 0.05).sum())
        lmax = min(max(LAGS), a.M // 5)
        ci = ci95(a.M)
        for k, x in series.items():
            rho = acf_matrix(x, lmax)
            for j in range(P.k_burst):
                krows[len(krows) - P.k_burst + j][f"sig1_{k}"] = int(abs(rho[j, 1]) > ci)
            for lag in LAGS:
                r[f"rho{lag}_{k}"] = rho[:, lag].mean()
                r[f"sig{lag}_{k}"] = int((np.abs(rho[:, lag]) > ci).sum())
            r[f"dfa_{k}"] = np.mean([projection_alpha(x[:, j]) for j in range(P.k_burst)])
        rows.append(r)
        print(f"{f.name:32s} alpha traj {r['alpha_traj_orig']:.3f} fgn1 {r['alpha_traj_fgn1']:.3f} "
              f"fgn2 {r['alpha_traj_fgn2']:.3f} (a0 {r['alpha0_fgn2']:.3f})  B/Bs orig {r['orig_surr']:.3f} "
              f"fgn1 {r['fgn1_surr']:.3f} fgn2 {r['fgn2_surr']:.3f}  DFA {r['dfa_orig']:.3f}/{r['dfa_fgn1']:.3f}/{r['dfa_fgn2']:.3f}",
              flush=True)

    df, dq = pd.DataFrame(rows), pd.DataFrame(qrows)
    out = Path(args.out)
    df.to_csv(out.with_suffix(".csv"), index=False)
    dq.to_csv(out.parent / (out.name + "_by_q.csv"), index=False)
    dk = pd.DataFrame(krows)
    dk.to_csv(out.parent / (out.name + "_by_k.csv"), index=False)

    n = len(df)
    L = ["# E2: FGN surrogate matched after filtering (FGN2) vs the pipeline FGN (FGN1)\n",
         f"{n} texts, q = {P.quantile} unless stated. alpha: DFA of the rank sequence of the M trajectory tokens "
         f"(estimator of the FGN-matching step). Bisection range for FGN2: [{LOW}, {HIGH}].\n",
         "## Rank-level matching\n"]
    d1 = df.alpha_traj_fgn1 - df.alpha_traj_orig; d2 = df.alpha_traj_fgn2 - df.alpha_traj_orig
    L.append(f"- FGN1 - orig: mean {d1.mean():+.3f} (sd {d1.std(ddof=1):.3f}, range [{d1.min():+.3f}, {d1.max():+.3f}])")
    L.append(f"- FGN2 - orig: mean {d2.mean():+.3f} (sd {d2.std(ddof=1):.3f}, max |.| {d2.abs().max():.3f}); "
             f"alpha0_fgn2 range [{df.alpha0_fgn2.min():.3f}, {df.alpha0_fgn2.max():.3f}]; "
             f"seed changes (non-convergence restarts): {int((df.seed_fgn2 != P.fgn_seed).sum())}")
    L.append("\n## Burstiness, per-text means over k (q = 0.95)\n")
    for c, lab in [("orig_surr", "orig/surr"), ("fgn1_surr", "FGN1/surr"), ("fgn2_surr", "FGN2/surr")]:
        s = df[c]; tt = ttest_1samp(s, 1.0)
        L.append(f"- {lab}: mean {s.mean():.4f} ± s.e. {s.std(ddof=1)/np.sqrt(n):.4f} (sd {s.std(ddof=1):.4f}), "
                 f"range [{s.min():.3f}, {s.max():.3f}]; t vs 1 = {tt.statistic:.2f}, P = {tt.pvalue:.2g}")
    tt = ttest_rel(df.fgn2_surr, df.fgn1_surr)
    L.append(f"- FGN2/surr - FGN1/surr: mean {(df.fgn2_surr - df.fgn1_surr).mean():+.4f}, paired t = {tt.statistic:.2f}, P = {tt.pvalue:.2g}")
    L.append(f"- full ordering at q = 0.95 with FGN2: {int(df.order_fgn2.sum())}/{20*n} pairs (FGN1: {int(df.order_fgn1.sum())}/{20*n}); "
             f"|B_FGN2/B_surr - 1| < 0.05 in {int(df.n_fgn2_within5.sum())}/{20*n}")
    L.append("\nBy q (full ordering, % of pairs):\n")
    L.append("| q | FGN1 | FGN2 | mean FGN1/surr | mean FGN2/surr |"); L.append("|---|---|---|---|---|")
    for q, s in dq.groupby("q"):
        L.append(f"| {q} | {100*s.order_fgn1.sum()/(20*len(s)):.1f}% | {100*s.order_fgn2.sum()/(20*len(s)):.1f}% | "
                 f"{s.fgn1_surr.mean():.4f} | {s.fgn2_surr.mean():.4f} |")
    L.append("\n## Projection ACF and DFA (means over texts of per-text means over k)\n")
    L.append("| quantity | orig | FGN1 | FGN2 |"); L.append("|---|---|---|---|")
    for lag in LAGS:
        L.append(f"| rho({lag}) | {df[f'rho{lag}_orig'].mean():.4f} | {df[f'rho{lag}_fgn1'].mean():.4f} | {df[f'rho{lag}_fgn2'].mean():.4f} |")
        L.append(f"| % (text,k) significant at lag {lag} | {100*df[f'sig{lag}_orig'].sum()/(20*n):.1f}% | "
                 f"{100*df[f'sig{lag}_fgn1'].sum()/(20*n):.1f}% | {100*df[f'sig{lag}_fgn2'].sum()/(20*n):.1f}% |")
    L.append(f"| DFA of projections | {df.dfa_orig.mean():.3f} | {df.dfa_fgn1.mean():.3f} | {df.dfa_fgn2.mean():.3f} |")
    L.append("\n## By component (q = 0.95): mean over texts of B/B_surr, % lag-1 ACF significant\n")
    L.append("| k | FGN1/surr | FGN2/surr | FGN1 sig(1) | FGN2 sig(1) |"); L.append("|---|---|---|---|---|")
    dk = dk.assign(r1=dk.B_fgn1 / dk.B_surr, r2=dk.B_fgn2 / dk.B_surr)
    for k, s in dk.groupby("k"):
        L.append(f"| {k} | {s.r1.mean():.4f} | {s.r2.mean():.4f} | {100*s.sig1_fgn1.mean():.0f}% | {100*s.sig1_fgn2.mean():.0f}% |")
    hi = dk[dk.k >= 4]
    L.append(f"| k >= 4 | {hi.r1.mean():.4f} | {hi.r2.mean():.4f} | {100*hi.sig1_fgn1.mean():.0f}% | {100*hi.sig1_fgn2.mean():.0f}% |")
    L.append("\n## Per text (q = 0.95)\n")
    L.append("| file | genre | M | alpha orig | alpha FGN1 | alpha FGN2 | alpha0 FGN2 | orig/surr | FGN1/surr | FGN2/surr | DFA orig | DFA FGN2 |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for _, r in df.iterrows():
        L.append(f"| {r.file[:-4]} | {r.genre} | {r.M:,} | {r.alpha_traj_orig:.3f} | {r.alpha_traj_fgn1:.3f} | {r.alpha_traj_fgn2:.3f} | "
                 f"{r.alpha0_fgn2:.3f} | {r.orig_surr:.3f} | {r.fgn1_surr:.4f} | {r.fgn2_surr:.4f} | {r.dfa_orig:.3f} | {r.dfa_fgn2:.3f} |")
    out.with_suffix(".md").write_text("\n".join(L) + "\n")
    print("\n".join(L[:40]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
