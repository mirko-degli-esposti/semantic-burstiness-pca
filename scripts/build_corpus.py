"""Build a cleaned corpus from Project Gutenberg texts, driven by a manifest.

Input:  data/pg/text/PG<id>_text.txt  (scripts/pg_fetch.py get: Gutenberg header/footer removed)
        <out>/manifest.csv            one row per text: file, pg_id, ..., start, end
Output: <out>/<file>                  body of the work, normalised (see clean())
        <out>/build_report.csv        per-text sizes and residual checks

Body: from the first match of `start` to the end of the last match of `end`.  Both are
word sequences matched case-insensitively with any non-word characters in between, so
they are insensitive to punctuation, quotes and line breaks.  The rule used when choosing
them: the work's own text, from the first chapter (or the author's integral introduction)
to the end of the last chapter, epilogue or conclusion; prefaces, contents, lists of
illustrations, etymologies/extracts, appendices, indices and notes are excluded.

The result is then passed unchanged to semburst.text.tokenise (NLTK word_tokenize on the
lower-cased text, alphabetic tokens only).

Usage:
    python scripts/build_corpus.py                       # data/corpus_v2
    python scripts/build_corpus.py --out data/corpus_v2 --only ulysses.txt
"""
import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

PG_TEXT = Path("data/pg/text")

LIGATURES = {"æ": "ae", "Æ": "Ae", "œ": "oe", "Œ": "Oe", "ß": "ss"}
QUOTES = {"‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
          "“": '"', "”": '"', "„": '"', "«": '"', "»": '"'}
DASHES = {"—": " -- ", "–": " -- ", "―": " -- "}
ABBREV = re.compile(r"\b(Mr|Mrs|Messrs|Dr|St|Mt|Mme|Mlle)\.")
HEADING = re.compile(r"^[ \t]*(CHAPTER|Chapter|BOOK|Book|PART|VOLUME|LECTURE)[ \t]+"
                     r"([IVXLCDM]+|\d+|[A-Z]+)\b[.:]?", re.M)
SECTION_NUM = re.compile(r"^[ \t]*[-—]*[ \t]*([IVXLCDM]+|\d+)[ \t]*[-—]*[ \t]*\.?[ \t]*$", re.M)
BRACKETS = [
    re.compile(r"\[_?Copyright[^\]]*\]"),                    # inside Pride's illustrations
    re.compile(r"\[(Illustration|picture|map)[^\]]*\]", re.S),
    re.compile(r"\[(Footnote|Sidenote|Transcriber)[^\]]*\]", re.S),
    re.compile(r"^\[\d+\][^\n]*(\n[^\n]+)*", re.M),          # footnote paragraphs "[1] ..."
    re.compile(r"\[\s*\d+\s*\]"),                           # footnote refs, Ulysses "[ 1 ]"
    re.compile(r"^Footnote \d+:?[ \t]*\n(?:[ \t]*\n)?(?:[ \t]+\S[^\n]*\n?)+", re.M),  # Smith: indented block
]
IMAGE_LINES = re.compile(r"^[ \t]*(\S+\.(jpg|png|gif) \(\d+K\)|Full Size)[ \t]*$", re.M)
EXTRA_LINES = re.compile(r"^[ \t]*(_Pages_ [\d\-]+|(End of )?Phase the \w+(:[^\n]*)?)[ \t]*$", re.M)


def words_pattern(snippet: str) -> re.Pattern:
    return re.compile(r"\W+".join(map(re.escape, re.findall(r"\w+", snippet))), re.I)


def body(text: str, start: str, end: str, name: str) -> str:
    s = list(words_pattern(start).finditer(text))
    e = list(words_pattern(end).finditer(text))
    if not s or not e:
        raise SystemExit(f"{name}: start/end snippet not found ({len(s)}, {len(e)})")
    if len(s) > 1:
        print(f"  warning {name}: start snippet matches {len(s)} times, using the first")
    i, j = s[0].start(), e[-1].end()
    if j <= i:
        raise SystemExit(f"{name}: end before start")
    return text[i:j]


def clean(text: str) -> str:
    for rx in BRACKETS:
        text = rx.sub(" ", text)
    text = IMAGE_LINES.sub("", text)
    text = EXTRA_LINES.sub("", text)             # Wallace page ranges, Tess "Phase the ..." headings
    text = HEADING.sub("", text)                # "CHAPTER XII." label only; the title is kept
    text = SECTION_NUM.sub("", text)             # lines holding only a section numeral
    text = text.translate(str.maketrans({**QUOTES, **LIGATURES, **DASHES}))
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^\x00-\x7f]+", " ", text)    # leftover symbols and non-Latin script (Greek in Mill)
    text = text.replace("_", "").replace("=", "")   # _italics_, =bold= (James)
    text = ABBREV.sub(r"\1", text)               # "Mr." -> "Mr" (kept as a word)
    text = re.sub(r"(?<=[A-Za-z])-(?=[A-Za-z])", " ", text)   # to-day, good-natured -> two words
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="data/corpus_v2")
    ap.add_argument("--only", nargs="*")
    args = ap.parse_args()
    out = Path(args.out)
    rows = list(csv.DictReader(open(out / "manifest.csv", encoding="utf-8")))
    if args.only:
        rows = [r for r in rows if r["file"] in args.only]

    from semburst.text import tokenise
    report = []
    for r in rows:
        raw = (PG_TEXT / f"PG{r['pg_id']}_text.txt").read_text(encoding="utf-8")
        b = body(raw, r["start"], r["end"], r["file"])
        txt = clean(b)
        (out / r["file"]).write_text(txt, encoding="utf-8")
        toks = tokenise(txt)
        n = len(toks)
        single = sum(1 for t in toks if t in {"s", "t", "d", "ll", "ve", "re", "m"})
        report.append({
            "file": r["file"], "pg_id": r["pg_id"], "chars_pg": len(raw), "chars_body": len(b),
            "body_%": round(100 * len(b) / len(raw), 1), "N_all": n,
            "non_ascii_chars": sum(1 for c in txt if ord(c) > 127),
            "brackets_left": txt.count("["), "contraction_fragments_per_1k": round(1000 * single / n, 2),
            "mr_mrs": sum(1 for t in toks if t in {"mr", "mrs"}),
        })
        print(f"{r['file']:32s} body {report[-1]['body_%']:5.1f}%  N={n}")
    keys = report[0].keys()
    path = out / ("build_report.csv" if not args.only else "build_report_partial.csv")
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, keys); w.writeheader(); w.writerows(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
