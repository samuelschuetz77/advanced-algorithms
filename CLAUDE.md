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

## Never edit code in `projects or assignments i turn in live here/`

This is graded, submitted coursework — same category as `learning log.md`:
it must stay student-authored, per the class's academic integrity rules.
Claude must **never edit, complete, or fix** files in this folder unless the
student explicitly asks for that specific change in that moment.

- If the student is debugging (e.g. a traceback, an import error), diagnose
  and explain the error, but don't also fix unrelated bugs or finish
  unfinished logic sitting nearby in the same file — even if it looks
  broken or incomplete. That's the student's to write.
- Only touch these files when the student explicitly says to fix, finish,
  write, or edit specific code here. Answering "why is this broken" is not
  that request.
- This applies to any agent/subagent working in this repo, not just the
  top-level session.

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
   - **Scope every git command in this flow to this repo specifically**,
     regardless of which directory Claude was invoked in — this repo is a
     submodule of `senior`, so where the diff/tag actually lands depends on
     cwd. See "Running this flow from senior root vs. from inside this
     repo" below before running anything.
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

## Running this flow from senior root vs. from inside this repo

This repo is a git submodule of `senior`. The learning log flow (diff since
last `submitted-*` tag, tagging on submission) uses `git diff` and `git tag`,
which always operate on whatever repo the *current working directory* (or
`git -C <path>`) resolves to — not on "the repo the file logically belongs
to." That means the correct invocation depends on where Claude was clauded
into:

- **Clauded into this repo directly** (`advanced algorithms/` is cwd, or a
  session started here): plain `git diff`, `git log`, `git tag` just work —
  they're already scoped to this repo. No special handling needed.

- **Clauded into `senior` root**: plain `git diff`/`git tag` from root hit
  the *root* repo, not this one. From root's point of view this whole
  folder is a single opaque gitlink entry — root's git has no idea
  `learning log.md` exists, so an un-scoped `git diff` here will show
  nothing useful (or the wrong thing entirely), and an un-scoped `git tag
  submitted-...` would tag the *root* repo's history instead of this one,
  silently doing the wrong thing. From root, every command in this flow
  must be explicitly scoped, e.g.:
  - `git -C "advanced algorithms" diff submitted-2026-01-01 -- "learning log.md"`
  - `git -C "advanced algorithms" tag submitted-2026-01-15`
  - `git -C "advanced algorithms" push origin submitted-2026-01-15`
  (or `cd "advanced algorithms"` first, run the flow, then return to root —
  either is fine, but don't run these commands un-scoped from root.)

- **Tagging never needs a root-side step.** Creating `submitted-YYYY-MM-DD`
  labels an existing commit in this repo — it doesn't create a new commit,
  so it does *not* trigger the "bump the root pointer" rule from the root
  `AGENTS.md`. The root pointer only needs updating if the tagged commit
  itself was new and unpushed (i.e. normal submodule-commit handling
  applies to the underlying commit, not to the act of tagging it). Do push
  the tag to this repo's own remote (`git push origin <tag>`) so it's not
  just local.

- **Report file paths are relative to this repo**, not to `senior` root —
  `generated-ai-use-reports/...` means
  `advanced algorithms/generated-ai-use-reports/...` when working from root.

## Class notes

Whenever "class notes" come up, see `class-notes-fetching.md` — it points to
the live published Google Doc URL to `WebFetch` rather than relying on a
stale local copy.

## Scraping Canvas assignment pages with claude-in-chrome

Canvas assignment pages often hide content behind collapsible/dropdown
sections (e.g. an "Example code" toggle under "Optional Starter Code and
Ideas"). A plain page read can silently miss that content and leave the
local `Assignments/*.md` copy incomplete without any obvious sign something
was skipped — this already happened once with `Project 1 - Sorting.md`,
which shipped with a "not captured here, re-check the assignment page"
placeholder instead of the actual example code.

When transcribing a Canvas assignment page into this repo via
claude-in-chrome: before extracting/copying content, click through and
expand every collapsible section, dropdown, or "show more"/dropdown-arrow
control on the page so nothing is left collapsed, then capture the fully
expanded page content.

## Notes

- `todo.md` is scratch/setup tracking, not part of the graded product.
- Transcripts pasted in for report generation aren't auto-saved as files
  unless the student asks — the report is the durable artifact.
