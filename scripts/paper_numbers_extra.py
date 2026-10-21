"""Numbers quoted in the paper that paper_numbers.py does not compute: dependence of the
per-text ratio on M and on genre, event counts and estimator errors behind the q = 0.99
discussion, failures of the full ordering, and the semantic-pole tables of the four
showcase texts (scripts/poles.py format).

Usage:
    python scripts/paper_numbers_extra.py data/corpus_v2 --results results_v2 \\
        --manifest data/corpus_v2/manifest.csv --out results_v2/paper_numbers_extra.md \\
        --showcase war_and_peace.txt origin_of_species.txt great_expectations.txt ulysses.txt
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu, pearsonr, spearmanr, ttest_ind

sys.path.insert(0, str(Path(__file__).parent))
from poles import latex_rows                                        # noqa: E402
from semburst.burst import burstiness_spectrum, thresholds          # noqa: E402
from semburst.config import DEFAULT as P                            # noqa: E402
from semburst.embed import load_vectors                             # noqa: E402
from semburst.pipeline import analyse_text                          # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus_dir")
    ap.add_argument("--results", default="results_v2")
    ap.add_argument("--manifest", default="data/corpus_v2/manifest.csv")
    ap.add_argument("--out", default="results_v2/paper_numbers_extra.md")
    ap.add_argument("--showcase", nargs="+",
                    default=["war_and_peace.txt", "origin_of_species.txt", "great_expectations.txt", "ulysses.txt"])
    ap.add_argument("--pcs", type=int, nargs="+", default=[1, 2, 3])
    args = ap.parse_args()
    L = ["# Additional paper numbers\n"]
    w = L.append

    b = pd.read_csv(Path(args.results) / "corpus_burstiness.csv")
    man = pd.read_csv(args.manifest).set_index("file")
    q = b[b.q == 0.95]
    pt = q.assign(r=q.B_orig / q.B_surr_mean).groupby("file").agg(r=("r", "mean"), M=("M_filtered", "first"),
                                                                    N=("N_all", "first"))
    pt["genre"] = man.genre
    w("## Per-text ratio <B_orig/B_surr>_k at q = 0.95\n")
    r, p = pearsonr(pt.r, pt.M); rs, ps = spearmanr(pt.r, pt.M)
    w(f"- vs M: Pearson r = {r:.3f} (P = {p:.2f}), Spearman rho = {rs:.3f} (P = {ps:.2f}), n = {len(pt)}")
    g = pt.groupby("genre").r
    for gen, s in g:
        w(f"- {gen}: n = {len(s)}, mean {s.mean():.3f} ± s.e. {s.std(ddof=1)/np.sqrt(len(s)):.3f} "
          f"(sd {s.std(ddof=1):.3f}), range [{s.min():.3f}, {s.max():.3f}]")
    fi, nf = pt[pt.genre == "fiction"].r, pt[pt.genre == "nonfiction"].r
    tt = ttest_ind(nf, fi, equal_var=False); mw = mannwhitneyu(nf, fi, alternative="two-sided")
    w(f"- nonfiction - fiction: {nf.mean() - fi.mean():.3f}; Welch t = {tt.statistic:.2f}, P = {tt.pvalue:.2g}; "
      f"Mann-Whitney U = {mw.statistic:.0f}, P = {mw.pvalue:.2g}")
    ranks = pt.r.rank(ascending=False)
    w(f"- ranks of the nonfiction texts (1 = highest of {len(pt)}): {sorted(int(x) for x in ranks[pt.genre == 'nonfiction'])}")
    r2, p2 = pearsonr(fi, pt[pt.genre == "fiction"].M)
    w(f"- fiction only, vs M: Pearson r = {r2:.3f} (P = {p2:.2f})\n")

    w("## Event counts and estimator error, n = (1-q) M, relative error ~ 1/sqrt(n)\n")
    Ms = pt.M
    for label, M in [("median M", float(Ms.median())), ("shortest M", float(Ms.min())), ("longest M", float(Ms.max()))]:
        cells = ", ".join(f"q={qq}: n={(1-qq)*M:,.0f}, 1/sqrt(n)={100/np.sqrt((1-qq)*M):.1f}%" for qq in (0.95, 0.99))
        w(f"- {label} = {M:,.0f}: {cells}")
    w(f"  (shortest: {Ms.idxmin()}; longest: {Ms.idxmax()})\n")

    w("## Full-ordering failures\n")
    for qq in P.q_sweep:
        s = b[b.q == qq]
        bad = s[~((s.B_orig > s.B_fgn) & (s.B_orig > s.B_surr_mean))]
        w(f"- q={qq}: {len(bad)} of {len(s)} pairs" + (": " + ", ".join(f"{f[:-4]} k={k}" for f, k in zip(bad.file, bad.k)) if len(bad) else ""))
    w("")

    w("## Semantic poles of the showcase texts (scripts/poles.py format, n = 6)\n")
    wv = load_vectors()
    for f in args.showcase:
        an = analyse_text(Path(args.corpus_dir) / f, wv)
        B = burstiness_spectrum(an.pca.proj, thresholds(an.pca.proj, P.quantile))
        kmax = int(np.argmax(B))
        pcs = sorted(set(args.pcs) | {kmax + 1})
        w(f"### {f}: B_max = {B[kmax]:.3f} at PC{kmax+1}\n")
        w("```latex")
        for i, pc in enumerate(pcs):
            w(latex_rows(an, wv, pc - 1, B[pc - 1], n=6, bold=(pc - 1 == kmax)))
            if i < len(pcs) - 1:
                w(r"\midrule")
        w("```\n")
    Path(args.out).write_text("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
