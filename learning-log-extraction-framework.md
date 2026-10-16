# Learning Log Extraction Framework

Use this when I say **"extract learning logs"**, **"find log entries in this chat"**, or a close variant. The source may be a pasted plain-text chat or the current Codex/Claude conversation. A paste is unnecessary when the relevant work is already in context. This is a conversation-first workflow; `learning log.md` changes only when I subsequently ask you to write the draft there.

## Goal

Let me start with real work and questions. Afterward, find the few questions, corrections, and insights worth logging, especially the smaller misconception beneath a broad question. Keep the general case clear before adding exceptions. Describe confusion as a normal conceptual gap; omit vulnerable personal commentary and irrelevant transcript detail from the entry.

## Procedure

1. Read the supplied transcript or relevant conversation context. For this course, follow the eight-field structure in `CLAUDE.md` and `assignment information/Learning Logs.md`. Draw entry content from my questions, reasoning, attempts, corrections, and insights I claimed or approved. Distinguish those from explanations the agent merely gave.
2. Ask once: **"Did any moment or idea from this session stick with you? You can say 'none' or 'not sure.'"** If I identify one, prioritize it. If I say none, am unsure, or do not answer while the conversation continues, infer the strongest candidates from the session and keep going. Do not turn this into a long interview.
3. Find at most 1-3 coherent entry candidates by default. Prefer a moment when I revised my mental model, corrected an attempted solution, asked the same thing in different ways, or finally restated an idea myself. A narrow confusion that unlocked the larger topic can be more useful than the topic's most impressive fact. Do not force an entry from a session with no meaningful evidence; say what is missing.
4. Draft the candidate entries **in chat**. Lead with the simple, broadly useful rule. Put each distinct insight in a bullet of **fewer than 20 words**. Preserve essential conditions when dropping them would make a statement wrong; put optional nuance after the core idea or omit it. Use concrete language and my wording where possible.
5. Make the **last Insight/Answer bullet** address the underlying confusion suggested by my questions. If the transcript shows that I resolved it, state the correction plainly. If resolution is uncertain, phrase it as an open question or next test, not as something I already learned. Do not invent a hidden misconception when there is no evidence.
6. Stop after the chat draft. Treat **"write these down in the log," "add this to the learning log," "log it,"** or an equally clear instruction as authorization to edit `learning log.md`. If I revise a candidate before that, use my revision. When asked to write, make the mechanical edit directly, preserve existing entries, and use placeholders for missing rubric values instead of guessing them.

## Candidate selection cues

Look for my phrases such as **"wait," "why," "I thought," "so does that mean," "I'm confused," "but then," "I assumed," "oh," "now I see,"** and **"what am I missing?"** Also look for:

- A repeated or reframed question after an explanation.
- An example or counterexample I supplied that exposed a bad assumption.
- A bug, failed prediction, or surprising output I investigated.
- A shift from repeating an agent's explanation to explaining the idea in my own words.
- A prerequisite concept hidden inside a larger question.
- A conclusion I can test or apply to the next problem.

These are search cues, not proof that I understood something. Give more weight to what I tried, corrected, or restated than to the agent's polished answer.

## Chat draft format

```markdown
## [extract_from_gpt_chat] : Learning Log [number or fill in]

- Question/Problem: [The actual question or problem from my work.]
- When Identified: [fill in]
- Importance (1-5): [fill in]
- How to Learn: [What I tried or a concrete next test; mark a new suggestion as a suggestion.]
- Insight/Answer:
  - [Broad idea, fewer than 20 words.]
  - [Practical consequence or use, fewer than 20 words.]
  - [Underlying confusion, corrected if demonstrated; otherwise an open question. Fewer than 20 words.]
- Hours Spent Learning: [fill in]
- Minutes Spent Documenting: [fill in]
- Confidence (1-5): [fill in]
```

The heading tag deliberately replaces the date and time so I can spot drafts needing review. Never invent a timestamp, duration, importance, or confidence score. Use the existing log's current Learning Log number only when it is clear from context; otherwise leave it open. On file write, keep the tag until I supply the date/time or explicitly ask to replace it.

## Quick review before presenting a draft

- Is each entry about something I actually worked through?
- Is the general rule immediately understandable without a list of caveats?
- Is every insight bullet fewer than 20 words?
- Is the final bullet the deeper confusion, and is its resolution honestly calibrated?
- Can I see which fields still need my own values?

## Useful follow-up prompts from me

- **"Extract learning logs from this chat."** Use the current session.
- **"Extract learning logs from this transcript: ..."** Use the pasted session.
- **"None struck me; pick the strongest one."** Infer without asking again.
- **"Make it more general."** Remove secondary conditions while keeping the core claim true.
- **"What was I really confused about?"** Name the probable prerequisite or mistaken assumption and show the evidence briefly.
- **"Write the second one down in the log."** Edit only the chosen candidate into `learning log.md`.
