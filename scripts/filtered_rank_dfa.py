"""E1: does the frequency filter weaken the rank-level memory of the FGN surrogate more than
that of the original text?

For every text, DFA exponent of the Zipf-rank sequence of the original and of its FGN
surrogate (the one used by the pipeline, seed P.fgn_seed), measured with exactly the
estimator of the FGN-matching step (semburst.dfa.dfa_exponent, scales 100 .. min(10000, n/4),
10 log-spaced scales) on three sequences:

  unfilt  all N tokens (the sequence on which alpha0 is tuned)
  filt    after the frequency filter (top-R types and types with freq < min_freq removed), N_filt
  traj    filt minus out-of-vocabulary tokens: the M tokens of the embedding trajectory

Ranks are those of the original frequency table for all sequences (a constant shift of the
ranks, as produced by re-ranking the filtered vocabulary, leaves DFA unchanged).  A
word-shuffled reference (one permutation of the traj sequence, seed 0) checks the estimator.

Usage:
    python scripts/filtered_rank_dfa.py data/corpus_v2 --manifest data/corpus_v2/manifest.csv \\
        --out results_v2/filtered_rank_dfa
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import ttest_rel, wilcoxon

from semburst.config import DEFAULT as P
from semburst.dfa import DFA_L_MIN, DFA_N_SCALES, dfa_exponent, rank_l_max
from semburst.embed import build_trajectory, load_vectors
from semburst.surrogates import fgn_surrogate
from semburst.text import load_text


def alpha(ranks: np.ndarray) -> float:
    """The estimator of the FGN-matching step (surrogates.fgn_surrogate / dfa.text_alpha)."""
    return dfa_exponent(ranks, DFA_L_MIN, rank_l_max(len(ranks)), DFA_N_SCALES)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus_dir")
    ap.add_argument("--manifest", default=None, help="manifest.csv with a genre column (optional)")
    ap.add_argument("--out", default="results_v2/filtered_rank_dfa")
    ap.add_argument("--texts", nargs="*")
    args = ap.parse_args()
    files = sorted(Path(args.corpus_dir) / f for f in args.texts) if args.texts else sorted(Path(args.corpus_dir).glob("*.txt"))
    genre = pd.read_csv(args.manifest).set_index("file").genre if args.manifest else None
    wv = load_vectors()
    key = wv.key_to_index

    rows = []
    for f in files:
        tt = load_text(f, P)
        fgn = fgn_surrogate(tt.tokens_all, seed=P.fgn_seed)
        rank_of = {w: r for r, (w, _) in enumerate(tt.freq.most_common(), start=1)}
        keep = lambda t: t not in tt.stopset and tt.freq[t] >= P.min_freq
        seqs = {}
        for name, toks in [("orig", tt.tokens_all), ("fgn", fgn.tokens)]:
            filt = [t for t in toks if keep(t)]
            traj = [t for t in filt if t in key]
            seqs[name] = {s: np.array([rank_of[t] for t in x], dtype=np.float64)
                          for s, x in [("unfilt", toks), ("filt", filt), ("traj", traj)]}
        _, pos = build_trajectory(tt.tokens_filtered, wv)
        assert len(pos) == len(seqs["orig"]["traj"]) == len(seqs["fgn"]["traj"])
        shuf = seqs["orig"]["traj"][np.random.default_rng(0).permutation(len(seqs["orig"]["traj"]))]
        r = {"file": f.name, "genre": genre.get(f.name, "") if genre is not None else "",
             "N": tt.N_all, "N_filt": tt.N_filt, "M": len(pos),
             "alpha0": fgn.alpha0, "alpha_match_target": fgn.alpha_text, "alpha_match_fgn": fgn.alpha_surr}
        for s in ("unfilt", "filt", "traj"):
            r[f"orig_{s}"] = alpha(seqs["orig"][s])
            r[f"fgn_{s}"] = alpha(seqs["fgn"][s])
            r[f"diff_{s}"] = r[f"fgn_{s}"] - r[f"orig_{s}"]
        r["shuf_traj"] = alpha(shuf)
        rows.append(r)
        print(f"{f.name:32s} unfilt {r['orig_unfilt']:.3f}/{r['fgn_unfilt']:.3f}  "
              f"filt {r['orig_filt']:.3f}/{r['fgn_filt']:.3f}  traj {r['orig_traj']:.3f}/{r['fgn_traj']:.3f}  "
              f"shuf {r['shuf_traj']:.3f}", flush=True)

    df = pd.DataFrame(rows)
    out = Path(args.out)
    df.to_csv(out.with_suffix(".csv"), index=False)

    L = ["# E1: DFA of filtered rank sequences, original vs FGN\n",
         "Estimator of the FGN-matching step: `dfa_exponent`, L = 100 .. min(10000, n/4), 10 scales; "
         "ranks of the original frequency table. orig/fgn = alpha of the original / FGN rank sequence; "
         "diff = fgn - orig.\n",
         "| file | genre | N | M | alpha0 | unfilt orig | unfilt FGN | filt orig | filt FGN | traj orig | traj FGN | diff traj | shuf traj |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for _, r in df.iterrows():
        L.append(f"| {r.file[:-4]} | {r.genre} | {r.N:,} | {r.M:,} | {r.alpha0:.3f} | {r.orig_unfilt:.3f} | {r.fgn_unfilt:.3f} | "
                 f"{r.orig_filt:.3f} | {r.fgn_filt:.3f} | {r.orig_traj:.3f} | {r.fgn_traj:.3f} | {r.diff_traj:+.3f} | {r.shuf_traj:.3f} |")
    L.append("\n## Summary over texts (paired)\n")
    for s in ("unfilt", "filt", "traj"):
        d = df[f"diff_{s}"]
        tt = ttest_rel(df[f"fgn_{s}"], df[f"orig_{s}"]); wx = wilcoxon(d)
        L.append(f"- {s}: orig {df[f'orig_{s}'].mean():.3f} ± {df[f'orig_{s}'].std(ddof=1):.3f}, "
                 f"FGN {df[f'fgn_{s}'].mean():.3f} ± {df[f'fgn_{s}'].std(ddof=1):.3f}; "
                 f"diff mean {d.mean():+.3f} (sd {d.std(ddof=1):.3f}, range [{d.min():+.3f}, {d.max():+.3f}]), "
                 f"FGN < orig in {int((d < 0).sum())}/{len(d)}; paired t = {tt.statistic:.2f}, P = {tt.pvalue:.2g}; "
                 f"Wilcoxon P = {wx.pvalue:.2g}")
    L.append(f"- drop from unfilt to traj: orig {(df.orig_traj - df.orig_unfilt).mean():+.3f}, "
             f"FGN {(df.fgn_traj - df.fgn_unfilt).mean():+.3f}")
    L.append(f"- shuffled traj: {df.shuf_traj.mean():.3f} ± {df.shuf_traj.std(ddof=1):.3f}")
    L.append(f"- check: alpha_match_target == orig_unfilt to 1e-9: {bool(np.allclose(df.alpha_match_target, df.orig_unfilt, atol=1e-9))}; "
             f"|alpha_match_fgn - fgn_unfilt| max {np.abs(df.alpha_match_fgn - df.fgn_unfilt).max():.2g}")
    if genre is not None:
        L.append("\nBy genre (traj):\n")
        for g, s in df.groupby("genre"):
            L.append(f"- {g}: n = {len(s)}, orig {s.orig_traj.mean():.3f}, FGN {s.fgn_traj.mean():.3f}, "
                     f"diff {s.diff_traj.mean():+.3f} ± {s.diff_traj.std(ddof=1)/np.sqrt(len(s)):.3f} (s.e.)")
    out.with_suffix(".md").write_text("\n".join(L) + "\n")
    print("\n".join(L[-12:]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
