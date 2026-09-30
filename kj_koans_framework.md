# KJ Koans framework

Use this guide to turn **any supplied reading, notes, or source text** into a small static study artifact inspired by the ClojureScript Koans interaction. It must run on localhost and can also be published as static files. The learner sees **one short statement with exactly one missing word**, enters that word, and moves to the next statement.

## Inputs

1. Identify the exact source and scope: file, chapter/section, page range, pasted text, or URL. If a source is available in the workspace, read it directly. If it is missing, ask for it rather than inventing source-specific claims.
2. Record the learner's requested emphasis. Cover that emphasis first, then the rest of the scoped material. For a course, read the posted schedule and create one set for every assigned reading section that has a verifiable source. Record inaccessible readings as source gaps rather than silently inventing their contents.
3. Extract a small concept map: definitions, implications, examples, limits, and common confusions. Mark claims that are conjectures or open questions so the koans preserve their uncertainty.

## Write the koans

Create roughly 6–10 koans per section, adjusted to the density of the source. Order them so one idea prepares for the next. Teach a concept before asking the learner to recall its name. Prioritize predictions, consequences, distinctions, and decision rules over isolated vocabulary.

Each koan must have:

- `before` and `after`: the two parts of a natural sentence surrounding **one** missing word.
- `answer`: one canonical word. Accept a few equivalent single-word answers when the sentence genuinely allows them.
- `section`: the source section or topic for coverage auditing. Do not display section navigation in the exercise.
- `code` (optional): a short, read-only snippet shown above the sentence. Keep **every blank in the sentence**, never in the code. Aim for 3–5% of all koans to reference code. Use Python for general programming and algorithms; use the reading's language when the language itself is the concept (for example TypeScript or React).

Write original, plain-language sentences rather than copying the source. Test one idea per sentence. The missing word should matter conceptually; never blank an article, preposition, or other function word merely to complete the grammar. Avoid trivia, ambiguous grammar, or blanks that can be answered from punctuation alone. Prefer a precise sentence over a clever one. For technical notation, keep the notation outside the blank when the answer is meant to be a word.

Check every sentence against its source. In particular, distinguish a known algorithm from a proved lower bound, a necessary condition from a sufficient one, and an implication from its converse. For reductions, state the arrow's direction and what an efficient transformation preserves. Re-read a sentence with each plausible alternative answer: either accept a genuine synonym or rewrite the sentence to make the intended answer clear. Avoid making the learner guess a short word already implied by grammar. If the answer is `no`, place the blank under `no`, with a two- or three-character underline.

## Visual design and interaction contract

The exercise page contains the current sentence, its inline blank text box, an optional small code snippet when the question needs it, and a very small Restart button at the bottom. Center the sentence and blank with generous empty space. Use an off-white background and near-black text. Use a plain sans-serif font. No cursive or decorative type.

Do not show a title, introduction, header, sidebar, chapter list, preview of upcoming topics, question number, progress count or bar, instructions, hint control, Check button, Next button, or footer on the exercise page. The Restart button stays small and visually quiet at the bottom. For a multi-course collection, the home page has only the collection title and class links; each class page lists its reading sets. Navigation disappears once a set starts.

1. The learner types directly in the blank. A correct word turns the blank green and automatically advances after a brief pause.
2. Enter checks an incorrect word, turning the blank red. Editing clears the red state. The learner stays on the same sentence, with no penalty or answer reveal.
3. Save the next question index in `localStorage` so refresh resumes the session.
4. At the end, show only “Complete.” in the main area. The same small Restart button remains available at the bottom.

Keep the page keyboard usable, give the input an accessible label, and announce nonvisual feedback with `aria-live`. Make it work on narrow screens. Avoid a backend or dependency installation for a simple static artifact.

## Build and verify

For a standalone reading, place `index.html`, `style.css`, and `app.js` in its own directory. For a multi-course collection, share the UI and keep each course's koans in a separate structured data file. Give each reading set its own `localStorage` key. Keep schedule metadata and source provenance with the set data; do not publish source PDFs or private course files just to build the site.

Serve the directory on localhost, for example:

```powershell
python -m http.server 8000 --directory "koans/reading-name"
```

Verify in a browser: one sentence, its blank, and the small bottom Restart button are visible during questions; wrong input checked with Enter turns red; typing the correct word turns green and advances; refresh restores unfinished progress; completion is just “Complete.” plus Restart; the button resets progress; mobile width remains usable. Review every accepted answer for accidental ambiguity.

## Current example

`koans/jea-12-1-12-3/` applies this framework to Jeff Erickson's *Algorithms*, §§12.1–12.3. Its questions cover CircuitSat, P/NP/co-NP, NP-hardness, NP-completeness, and the direction and answer preservation of a polynomial-time reduction.
