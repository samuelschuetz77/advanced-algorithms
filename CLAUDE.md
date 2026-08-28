# This repo: Advanced Algorithms Learning Log

This repo holds exactly one gradeable product: `learning log.md`. Everything
else here (reports, transcripts, todo.md) is scaffolding around it.

## Directory convention (applies across all class repos in `Senior/`)

- `Assignments/` — assignment **descriptions and rubrics only** (specs,
  study guides, quiz notes). Never put actual submitted work here.
- `projects or assignments i turn in live here/` — the actual files that get
  submitted (e.g. `sorting.py` for Project 1). This is the analogous folder
  to `Assignments/` but for deliverables instead of specs.

This same split (`Assignments/` for specs, `projects or assignments i turn
in live here/` for submissions) is the convention for the other class repos
under `Senior/` (`frontend/`, `maintenance/`) too.

## The rules

- `learning log.md` contains **only log entries**, one per Question/Problem,
  each using the 8 rubric fields below, in this order, verbatim from the
  student — never AI-authored content:

  1. Question/Problem
  2. When Identified
  3. Importance (1-5)
  4. How to Learn
  5. Insight/Answer
  6. Hours Spent Learning
  7. Minutes Spent Documenting
  8. Confidence (1-5)

- Claude never writes log entry *content*. Claude may ask targeted questions
  field-by-field and transcribe the answer verbatim (punctuation/spelling/
  formatting cleanup only), or help fix formatting on existing text.

## "The learning log flow"

This is the recurring name for the whole process below — recognize this
phrase even if the user doesn't re-explain it.

1. **During learning** (usually a ChatGPT session, sometimes Claude Code):
   student works through a question by asking targeted questions, getting
   examples, etc.

2. **Editing the log**: student dictates field values; Claude transcribes
   them into `learning log.md` verbatim (cleanup only, no added content).

3. **"Generate text report" / "give me my thing" / etc.** — the trigger
   phrase for turn-in prep. When the student says this, Claude should:
   - Run `git diff` against the most recent `submitted-*` tag (or from the
     start of file history if no tag exists yet) on `learning log.md` to see
     what's new since last submission.
   - Ask the student if they have any chat transcripts (ChatGPT browser
     session copy/paste, or a Claude Code session) to include.
   - If given transcript(s), analyze them against the diffed log entries and
     produce:
     a. Clean Canvas-submittable log text (the diffed entries, formatted).
     b. An AI-use report, ≤500 words, saved to
        `generated-ai-use-reports/` (see naming below). This is **not a
        disclosure** — it's a report on where the student's understanding
        was during the session, useful for the instructor to see. Cover:
          - What questions the student asked.
          - What they seemed confused about, and whether it seemed to
            resolve (best signal: student restates the concept in their own
            words and it's accurate, or draws an analogy that's mostly
            right and just needs minor correction).
          - Best-guess areas still likely shaky — sometimes inferable only
            by reading between the lines (e.g., a question's phrasing
            implies a missing sub-concept the student needs before the
            parent concept can click). Flag uncertainty as uncertainty.
   - Also flag anything from the AI session that seems missing from the
     log entry but that the instructor would likely want documented (e.g.
     an insight that came up in chat but never made it into
     Insight/Answer).
   - Report file naming: `generated-ai-use-reports/YYYY-MM-DD-<short-topic-slug>.md`

4. **Student reviews**, may go edit `learning log.md` further based on what
   the report flagged as missing. Repeat step 3 as needed — nothing is
   final yet.

5. **Submission**: only when the student explicitly confirms they turned it
   in (e.g. "I submitted that," "mark this as submitted") does Claude tag
   the current commit `submitted-YYYY-MM-DD` so future diffs have a clean
   starting point. Never auto-tag on a report generation alone.

## Class notes

Whenever "class notes" come up, see `class-notes-fetching.md` — it points to
the live published Google Doc URL to `WebFetch` rather than relying on a
stale local copy.

## Notes

- `todo.md` is scratch/setup tracking, not part of the graded product.
- Transcripts pasted in for report generation aren't auto-saved as files
  unless the student asks — the report is the durable artifact.
