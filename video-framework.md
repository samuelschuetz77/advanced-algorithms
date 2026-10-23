# Advanced Algorithms Video Framework

Recognize these phrases even without the word "framework": "make a video",
"video series", "Khan Academy style video", "script for the video", "the video
framework".

This is the spec for every narrated study video made for this class. It
combines (a) Samuel's own requests for the 2026-10-22 series, (b) what was
learned from the first videos in `advanced algorithms/output/`, and (c) a critique of those
videos so the next ones are better, not copies.

Provenance: the only saved material from the earlier videos was
`output/kruskal-2026-10-12/` (narration.json, render_video.py, README) and
`output/huffman-week-2026-10-13-concrete/` (storyboard.json, build.py, README,
SRTs). The chat that produced them is not in the Claude Code transcripts, so no
earlier prompts were recoverable; their requirements are inferred from the
finished files.

---

## 1. What the viewer is trying to do

Samuel is a senior who missed or half-understood a lesson and wants to
**re-derive it by hand and explain it back**. A video succeeds when, with no
other context, he can: (1) redraw the example from memory, (2) run the
algorithm on paper, (3) say why it is correct in his own words, and (4) read
the Python without getting stuck on syntax.

The video is a tutor, not a summary. It must never be a lecture that only works
if you already know the topic.

## 2. The Khan Academy rules (Samuel's core requirement)

1. **Zero-context rule.** Every sentence may only use terms that were already
   defined, on screen, earlier in the same video (or are everyday English).
   If a term must appear first, give an example before the name, then the name.
2. **Concrete before abstract.** Order is always: a story or tiny example, then
   a name for what we just did, then the general rule, then the code or proof.
3. **Work one example slowly, all the way through.** One small anchor example
   per video, reused every beat. Prefer Samuel's own class drawings when they
   exist. Never switch examples mid-concept.
4. **Draw as we talk.** Nothing is on screen before it is mentioned. Things
   appear, get circled, or get colored at the exact word that names them. Dim
   everything that is not the current focus.
5. **State is always visible.** A permanent state panel shows the data
   structures (pile, visited set, parent table, output lists) and updates every
   step. The viewer should never have to remember a value that was said aloud.
6. **Ask, pause, then answer.** At every real decision point, stop and ask the
   viewer to predict (a visible "PAUSE AND PREDICT" chip with a 4 to 6 second
   silent countdown), then reveal. Aim for one prediction per 60 to 90 seconds.
7. **Name the misconception.** For each concept, say the wrong idea a student
   probably has ("you might think we mark a room when we write the note; watch
   why that breaks"), show it failing, then show the fix.
8. **Small steps, no jumps.** If a step needs a fact the viewer might not have,
   add a 10 second beat for that fact. Prefer too slow to too fast. Never
   say "obviously", "clearly", "simply", or "as we know".
9. **Recap by retelling.** End every video with the story in 3 sentences and
   one thing to try on paper. Open the next video with a 10 second callback.
10. **Warm and human.** Plain contractions, short sentences, an occasional
    rhetorical question, no hype. Sounds like someone explaining at a
    whiteboard, not a narrator reading a PDF.

## 3. Critique of the October videos (what to keep, what to fix)

Frames and files from `output/` (inside `advanced algorithms/`) were inspected directly.

**Keep**
- Full-sentence captions burned in, plus `.srt` files.
- One focus per scene; accent color per video; big readable headlines.
- Kruskal's graph + live "forest" panel updated after every decision. This is
  the model for the state panel (rule 5).
- Code introduced with a named helper instead of a lambda, and a side-by-side
  "version one vs version two" comparison.
- Computing totals twice as a cross-check (Huffman 98 bits).

**Fix**
| Problem seen | Why it hurts | Fix in the new series |
|---|---|---|
| Huffman videos are 1280x720 at **6 fps** (Kruskal 12 fps). Motion looks like a slideshow. | Hard to follow what changed between frames. | 1920x1080 at **30 fps** with eased motion. |
| Captions are the whole narration paragraph (3 lines, the same text as the audio). | Viewer reads instead of watching the picture; no extra information. | Short synced subtitles, two lines max, shown phrase by phrase on the spoken words. Key term highlighted. |
| Huffman scenes show generic circles and chips while paragraphs play. | The visual does not match the sentence, so nothing is "pointed at". | Word-synced highlights: the object lights up when it is spoken. |
| Kruskal scenes are one 40 second, 100+ word paragraph over a long animation. | Overload; no pause to think. | Beats of 8 to 15 seconds, 15 to 35 words, one visual change per beat. |
| Kruskal code slide shows ~24 lines at once, no line highlighting, narration talks about code that is not marked. | Viewer cannot find what is being described. | At most 12 lines at once; the line being read is highlighted and everything else dimmed; a "values now" strip beside it. |
| No prediction pauses, no "what would you do?" moments. | Passive watching; weak retention (passive-listening trap in the audio system README). | Mandatory predict-then-reveal beats. |
| Assumed prior knowledge (Kruskal started with `find`/`union` meaning already known). | Violates zero-context. | Introduce each idea through a tiny example first. |
| Trace values typed into the build scripts by hand. | Risk of an on-screen number that disagrees with real code. | Every trace is **generated by running the real code**; the script keeps `trace_check.py` next to it. |
| No explicit link to the book chapters. | Viewer cannot find the matching reading. | A book chip on screen ("JEA 5.5, PDF p.217") and a coverage checklist per video (section 8). |
| No distinction between the book's names and plain names. | Book uses `s, v, w, p, bag`; Samuel's code uses other names. | Always teach with readable names, flash the book's name once as "the book calls this ...". |

## 4. Beat design

A video is a list of **beats**. A beat is one idea and one visual change.

- Length: 8 to 15 seconds spoken (about 15 to 35 words at ~145 words per
  minute). Longer only for a deliberate "watch it run" animation.
- Every beat has: `screen` (what is drawn), `narration`, `cues` (word to
  highlight/draw), `pause` (seconds of silence after, default 0.4), and
  `book` (optional section reference).
- Structure of a video (7 to 9 minutes; split rather than exceed 10):
  1. Cold open: a concrete situation and a question (20 to 40 s).
  2. Name what we just did. Define terms one at a time.
  3. The rule in plain English (never pseudocode first).
  4. Worked example, with predictions.
  5. Why it works (the argument, in pictures, with a tiny domino/chain image).
  6. The code, read symbol by symbol where needed.
  7. Recap + one thing to try + callback to the next video.

## 5. Narration and voice

- Voice: neural TTS through `edge-tts` (installed here), male or female
  `en-US-...MultilingualNeural` voices. **Chosen: Ava**
  (`en-US-AvaMultilingualNeural`, rate -4%), picked by Samuel after an audition
  (`advanced algorithms/output/advanced-algorithms-2026-10-22/voice-audition/`). It stays for the
  whole series. Not the old robotic voice.
- Write for the ear:
  - Spell numbers and symbols as spoken: "big O of V plus E", "two E plus one".
  - Letters as vertex names: write "room A" (not a lone "A"); read acronyms as
    letters in the script ("D F S"). Run a pronunciation line in every audition.
  - Short sentences, one comma-thought at a time. Use sentence breaks, not
    semicolons.
  - Put the key term at the end of the sentence (that is where the highlight
    lands).
- Build: per-beat audio is synthesized with `boundary="WordBoundary"` so each
  word has a start time and duration. Cues and subtitles read those times, so
  highlights are locked to the spoken word, not guessed.
- Master: concatenate beats with 0.3 to 0.6 s of silence, `loudnorm` to about
  -16 LUFS, no music under explanations.

## 6. Subtitles

- Burned in **and** exported as `.srt`.
- Two lines maximum, about 42 characters per line, 1.5 to 6 seconds each,
  split at phrase boundaries; never on top of the diagram (own caption band at
  the bottom).
- Generated from the same word timings as the audio so they never drift.
- Key terms inside a subtitle are bold or accent colored when spoken.

## 7. Visual system

- 1920x1080, 30 fps. Layout: top bar (series, video title, book chip), left
  stage (about 68%), right state panel (about 32%), bottom caption band.
- Light background, one accent color per video, dark text, large type (headline
  64 px, body 36 px, code 30 px at least). Contrast must be readable on a phone.
- Motion: ease-in-out, 0.4 s for appearing, 0.25 s for highlight rings. Edges are
  drawn progressively. The "current" thing gets a ring and a pulse; visited
  things are filled; stale/dead things are faded.
- Consistent color language across the whole series:
  - current vertex: accent ring
  - visited: filled accent
  - waiting in the pile: outline only
  - skipped / stale: gray with a strike
  - parent edge: thick accent line
- Graphs are always laid out exactly like Samuel's class drawings when one
  exists. Credit: "from your 10/19 notes".

## 8. Book coverage ("exhaustive explanations")

Each video starts from a **coverage checklist** of the chapter text it claims to
cover: every definition, algorithm, lemma, proof idea, figure, and warning. Each
item is marked one of:
- `Covered` (with the beat number),
- `Moved to video N`, or
- `Skipped` plus the reason.

Source files: `Reading for Prep/JEA - Algorithms textbook (Erickson).pdf`
(**PDF page numbers**, printed page = PDF page - 18) and the same-named `.txt`.
Say PDF pages in chips because that is what Samuel opens. Quote the book's
names once, then use readable names.

## 9. Code on screen (Python only)

- Python, plain constructs. No lambda, comprehensions, `walrus`, decorators,
  or one-liners **unless** they are the lesson. If one must appear, it gets a
  dedicated beat sequence:
  1. show the line alone,
  2. highlight each symbol and name it ("the `@` says ...", "the colon
     starts the body", "the comma on the left unpacks the pair into two
     names"),
  3. run it on a tiny input and show the values,
  4. show the same thing in the plain version.
- Show at most 12 lines at a time. Highlight the line being read. A "values
  now" strip shows the variables for that line on the current step.
- Use readable names: `to_visit`, `came_from`, `current`, `neighbor`,
  `parent_of`, `visited`. Show the book's name in a chip only when it helps.
- All code on screen is actually executed by the build and its output used for
  the trace/state panel.
- Samuel's graded files (`projects or assignments i turn in live here/`) are
  never edited by a video build. Code from `exercises/.../mini-lab.py` may be
  shown as-is, and a corrected version is shown only as a separate "what would
  change" slide, never written back unless Samuel asks.

## 10. Pipeline and folder layout

```
output/advanced-algorithms-YYYY-MM-DD/      <- inside the advanced algorithms repo folder
  00-series-plan.md
  voice-audition/
  NN-slug/
    script.md            <- the reviewed script (single source of truth)
    storyboard.json      <- beats generated from script.md
    trace_check.py       <- real code that produces every trace shown
    audio/  frames/  clips/
    NN-slug.mp4  NN-slug.srt  README.md
```

Tools already present: `ffmpeg`/`ffprobe`, Pillow, numpy, `edge-tts 7.3.1`,
moviepy. Frames drawn with Pillow (supersampled for clean lines), assembled
with ffmpeg (the existing `render_video.py` and `build.py` files show the
earlier approach).

Workflow per video, always together with Samuel:
1. **Learning objectives + prerequisites** (what must be true after watching;
   what the video assumes).
2. **Coverage checklist** from the book.
3. **Script** (`script.md`) reviewed by Samuel in chat. Nothing is rendered
   before the script is approved.
4. **Trace check** run; numbers frozen.
5. **Draft render** (480p, fast) to check pacing and cue alignment.
6. **QA** (section 11), then final render, SRT, README.
7. **After-watching note**: what clicked / what is still fuzzy, appended to the
   series plan. If a log entry is wanted, use Samuel's words
   (`learning-log-extraction-framework.md`); videos never write the learning log.

## 11. QA checklist

- [ ] **Cold-viewer test:** read the narration top to bottom; every term was
      defined on screen before its first use.
- [ ] **Mute test:** with the sound off, captions plus pictures still teach.
- [ ] **Pause test:** the first frame of each prediction beat contains
      everything needed to answer it.
- [ ] **Sync test:** extract frames at 3 random cue times; the highlighted object
      matches the spoken word.
- [ ] Each trace value on screen equals `trace_check.py` output.
- [ ] Code on screen runs; fancy constructs have their symbol-by-symbol beats.
- [ ] Coverage checklist has no unmarked items.
- [ ] Subtitles: no overflow, no overlap with the diagram, SRT matches the burned
      captions.
- [ ] Audio: no clipping, even loudness, no word cut off at beat joins.
- [ ] Runtime 6 to 10 minutes; file opens in a normal player.

## 12. Things we deliberately do not do

- Do not read the book aloud; explain it and point to the page.
- Do not show dense tables as the main visual.
- Do not use more than one example graph in one video.
- Worked-example graphs must be big enough to be real: **at least 7 vertices
  and 12 edges** (Samuel's rule). Walk the first steps slowly, then
  fast-forward the repetitive tail with a visible counter; never shrink the
  graph to make the trace short.
- Each video picks one vivid story world for its anchor (the colony for
  video 01) and says plainly where the metaphor breaks (mole-rats cannot read).
- Do not say "just", "obviously", "trivially".
- Do not hide a limitation: when a claim is only stated (not proved) in the video, say
  so and name the book page that proves it.
- Do not edit coursework files or the learning log as a side effect of a video.

## 13. Samuel's standing notes (carry into every video)

Updated each time Samuel sends notes. Also saved in Claude's memory as `video-series-preferences`.

- Voice: Ava, for the whole series.
- Story vs graph: the graph is on screen from the first frame and never leaves; one named
  character (Wrinkles the naked mole-rat) does every action on it. Story word + graph word
  together once, then graph words. (He said "too much story" and then "not enough mole-rat";
  this rule is the settled answer.)
- Examples: at least 7 vertices and 12 edges.
- Work together, script first: paste short script chunks in chat, let him decide, then build.
- Round 1 notes on video 01: "all in all that video was great"; fix the A and E pronunciation (done, see section 14); do not reuse the mole-rat in later videos; make all six.

- Round 2 notes: the school-rumor anchor in video 02 was muddled (people as vertices clashed with the word "parent"). Choose a story whose words already match the graph words (metro: station, track, came from). Output lives in `advanced algorithms/output/`.

- Round 3 notes: a lesson about the DFS loop starting at different vertices needs an example with at least two start vertices (no incoming edges); the E graph from class had only one, so video 04 now uses dinner plus 'set the table'.

- Round 4 notes: never state a conclusion before the picture (video 06's "the rightmost vertex must point left" opened with no visual); show a concrete case first, then the name. Graph drawings used to teach topological order must be tangled, with arrows in every direction, and the line-up shown as a rearrangement, not already drawn left to right.

## 14. Lessons from building the 2026-10-22 series

**Pronunciation (Ava).** Phonetic respellings fail: "ay" is read as "I", "ess" as "as", "ee" as the word "Ee".
Use plain capital letters ({A}). Two further traps, both found by transcribing with Whisper:
- A bare capital E is swallowed ("E has" sounds like "He has"). The parser now adds a trailing period to a lone E.
- A letter glued to a vowel word runs together: "A pointed" is heard as "appointed", and "B's bar" as "These bar". Say "vertex A pointed", "task A first", "room A", "the bar for room B".
Check every video with `python ../common/verify_letters.py` and `../common/transcribe_beats.py <beat id>` (Whisper small.en; ignore "E2A"-style formatting noise, fix real mishearings).
Also: a sentence ending in a lone letter ("... to v.") can make the TTS merge it with the next word and break word timing; end such sentences on another word.

**Build engine.** `advanced algorithms/output/advanced-algorithms-2026-10-22/common/` is the shared engine (engine, widgets, graphview, chars, pipeline, buildlib, dfslog). Each video folder has `storyboard.py` (narration with `[[cue]]word` markers), `scenes*.py`, a `*log.py` that runs the real algorithm, and a 5-line `build.py` that must keep its `if __name__ == "__main__":` guard (the renderer uses worker processes). Video 01 keeps its own copy of the engine files.

**Deviations from this document in the 2026-10-22 videos (to fix next time).**
- Length: videos 01 (10:48) and 06 (11:39) exceed the 10 minute cap in section 4. Candidates to trim in 06: the footnote-3 beat and the "what if there might be a cycle" beat.
- Code lines on screen: the cap is 12. Video 01 shows 12 and video 03 shows 9, but video 04 (16 lines), video 05 (21 lines), and video 06 (16 lines) exceed it. Split long listings across two cards.

**What worked.** Predict-and-pause beats; always-visible state panels; word-synced subtitle highlighting; every number produced by running code; a story word and its graph word introduced together.
