# Python Setup — uv, native Windows, VS Code

How Python files in this repo get set up and run. This exists so that when
Samuel tells an agent in this directory "new file called `some_name.py`," the
agent can scaffold it correctly without re-deriving these decisions.

## Why these choices

- **`uv`** — explicitly recommended in `Assignments/Project 1 - Sorting.md`
  for managing deps (pytest, pandas, seaborn). Already installed (`uv
  0.11.15`) and confirmed working.
- **Native Windows, not WSL** — WSL is used elsewhere in this environment for
  things with Linux-specific tooling/build requirements. Nothing this class
  needs (pytest, pandas, seaborn, plain Python) has a WSL-only reason to
  exist; `uv` and Python 3.11 both run natively on Windows fine, and staying
  native avoids path-translation friction between the repo (Windows path)
  and a WSL Python interpreter.
- **Single project at repo root** — Project 1's submission is one flat file
  (`sorting.py`) that must run via `python -m pytest sorting.py` and `python
  sorting.py`. A single `pyproject.toml`/`.venv` at the repo root (rather than
  a project-per-file setup) keeps that runnable exactly as specified, and
  also covers ad-hoc practice files for working through book examples.

## One-time repo setup (already needed before any `.py` file is useful)

```
uv init --no-workspace
uv add pytest pandas seaborn
```

This creates `pyproject.toml` and a `.venv/` at the repo root. Re-run `uv add`
if a reading/assignment calls for another package later.

## VS Code

- Interpreter: point VS Code at `.venv/Scripts/python.exe` (uv creates this
  natively on Windows — no WSL remote connection needed for this repo).
- Use the non-AI-enabled **Classwork Profile** (see
  `Assignments/ClassworkProfile.md`) whenever writing or editing code here —
  this is a course policy, not optional.

## Running things

- Run a script: `uv run python <file>.py`
- Run its tests: `uv run pytest <file>.py` (or `uv run python -m pytest
  <file>.py` to match Project 1's exact required invocation)

`uv run` uses the repo's `.venv` automatically — no manual activation needed.

## New-file scaffold (what "spin up `some_name.py`" should produce)

A new `.py` file should get this skeleton and nothing more — no algorithm
logic, since writing that content is Samuel's work, not the agent's:

```python
"""
<name>
CS 4230 - Advanced Algorithms
<date>
"""

import pytest


# --- implementation ---


# --- tests ---


if __name__ == "__main__":
    pass
```

- Header comment (name/course/date) matches what Project 1 explicitly
  requires at the top of `sorting.py`; worth doing by default for any file
  since submissions tend to want it.
- `import pytest` + a tests section up front, since the course consistently
  wants pytest tests alongside implementations, not bolted on after.
- The agent creates the file and opens/scaffolds it — it does not fill in
  the implementation or tests unless explicitly dictated, same rule as
  `learning log.md`.

## File placement

- Formal submissions (e.g. `sorting.py` for Project 1) live in
  `projects or assignments i turn in live here/` — see the convention note
  in `CLAUDE.md`. `Assignments/` holds only assignment descriptions/rubrics,
  not the actual submitted files.
- Practice files working through book examples/exercises can go in a
  `practice/` folder (create it the first time it's needed) so they don't
  get confused with actual submissions.
