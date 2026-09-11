# Reading for Prep

Almost every "Reading for Prep" row on the Canvas course schedule points to one of a small handful of shared PDFs — the schedule just cites different page/section ranges within the same file each week. Downloaded here:

| File | Covers | Used for these readings |
|---|---|---|
| `JEA - Algorithms textbook (Erickson).pdf` | Jeff Erickson's *Algorithms* — the main textbook | Preface, 0.5-0.6, 1.6-1.7, Ch.1 Exercises, 2.4/2.5/2.8, 12.1-12.3, 3.4/3.5/3.9, 4.1/4.4/4.5, 7.2/7.4, 5.5/5.6, 6.1/6.2-6.3/6.5-6.6, Ch 6 Exercises, 8.3, 9.5-9.6, 10.0-10.3, 11.0-11.7, 12.0-12.3, 12.5-12.6/12.8/12.10/12.13-12.14, Extra A |
| `review - Data Structures (Sheehy).pdf` | Don Sheehy's data structures notes | "review" reading for 9/4 (Graphs and Heaps) |
| `JEA Induction notes.pdf` | Erickson's induction supplement | "JEA Induction.1-3" for 9/14 |
| `JEA Extra H - Linear Programming notes.pdf` | Erickson's LP appendix notes | "JEA Extra H.1-H.2" and "H.4-H.5" for 11/11 and 11/13 |

**Not downloaded as PDFs** — these are live external resources, not standalone files:
- **Big O Page** (due 9/2) — a Canvas page itself, not a PDF. Content mirrored into `../big-ideas-and-review.md`... actually see `../course-schedule.md` note; can copy in full if wanted.
- **QC 1-3** and **QC 4-6** (due 11/30, 12/2) — link to an O'Reilly Learning ebook (`learning.oreilly.com`), which is **paywalled/subscription-gated**. I don't have your O'Reilly login, so this wasn't fetched — check if Snow College provides free O'Reilly access via library, then download/read manually.
- **Q# in Y** (due 12/2) — links to learnxinyminutes.com/qsharp/, a live reference page, not a PDF.
- **QFT** (due 12/4) — links to a Microsoft Learn tutorial page, not a PDF.

Downloaded PDFs will be re-fetched/updated only if the Canvas schedule page changes its source links — check `../course-schedule.md`'s "Last synced" date.

## Looking up text quickly

Each PDF has a plain-text sibling (same name, `.txt`) extracted with `pdftotext -layout`, since the PDF renderer on this machine needs `pdftoppm`/poppler (installed via `winget install oschwartz10612.Poppler`, but the tool needs a fresh Claude Code process to pick up the PATH change). Grep the `.txt` file instead of opening the PDF — much faster for finding a section or exercise set, e.g.:

```
grep -n "Exercises" "JEA - Algorithms textbook (Erickson).txt"
```

then read the surrounding lines. Re-run `pdftotext -layout <file>.pdf <file>.txt` if a PDF is ever re-fetched/updated.
