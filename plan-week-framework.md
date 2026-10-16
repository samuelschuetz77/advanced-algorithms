# Plan Week Framework

## Purpose

Use this framework when the user asks to "plan week," "run plan week," or asks for a weekly plan around the next learning log.

The goal is to look at the next learning log, the assigned readings, this week's in-class notes, and the major assignment or project due at the end of the week, then create a plan that makes those pieces support each other.

The most important analysis step is figuring out what parts of the reading are relevant to the end-of-week assignment.

In other words: kill as many birds as possible with the same stone.

## What To Inspect First

1. Find the next learning log assignment.
2. Find all readings assigned for that same week.
3. Find quizzes, projects, or assignments due near the end of that week.
4. Open the actual reading source, not just the schedule title.
5. Read or inspect the assigned textbook sections enough to identify the main concepts, techniques, examples, and algorithms.
6. Open the end-of-week assignment spec if it is available.
7. Identify which reading concepts directly help with the assignment, and which reading concepts are background only.
8. Check the running `learning log.md` to see the user's recent log style, questions, and learning strategies.
9. Check assignment tracker files such as `assignment information/CURRENT.md` and `course-schedule.md`.
10. Read the dated entries for this week in the [Advanced Algorithms class notes](https://docs.google.com/document/d/1myCP67cjrqx2AyWydVwta9xzXENrrA1kTPUHECX5j5I/edit?tab=t.0#heading=h.ebst22x8k9e5). Check the relevant prior class entry when it feeds the week's assignment. Reopen the notes after later class meetings; future dated headings may be empty placeholders.

## How To Use In-Class Notes

- Treat AI-assisted notes as a record of what was discussed, not evidence that the student understands it. Start by assuming each concept still needs to be explained and tested in the student's own words.
- For each dated class entry, identify the main claim, example, and any gap or ambiguous wording. Compare technical claims with the assignment and assigned reading before relying on them; notes can be incomplete or mistaken.
- Convert a promising note into a specific question: What does it mean? Why does it work? Can the student make a small example, verify a candidate, or distinguish it from a nearby concept? Work through that question with the student before treating it as a learned insight.
- Monday learning logs should center on the Friday assignment: its requirements, first example, problem choice, verifier, or brute-force reasoning. Class notes can support that work, but should not displace it.
- Wednesday learning logs should also center on the Friday assignment if it is unfinished or only nearly complete. If the assignment is substantially done, use a concept from Monday's or Wednesday's class notes that the student cannot yet explain independently.
- Never turn copied AI-assisted notes straight into a learning-log Insight/Answer. A log entry must capture the student's actual question, attempted reasoning, correction, or demonstrated understanding. When rerunning a plan, obey any instruction to propose alternatives without editing `learning log.md`.
- Friday is for understanding the week's class notes after required submission work is done. Choose a check that fits the material: explain in the student's own words, trace a small example, compare two concepts, answer an essay-style question, or find and fix a mistaken claim. Essay questions are one optional tool, not a fixed test.

## Reading-To-Assignment Relevance

Before making the day-by-day plan, answer these questions:

1. What is the end-of-week assignment asking the user to do?
2. What concepts from the reading are needed for that assignment?
3. What textbook examples are closest to the assignment?
4. What parts of the reading or class notes can become genuine learning log questions after the student works through them?
5. What parts of the reading can be safely skimmed unless the user has extra time?

The weekly plan should prioritize the reading sections that support the assignment. General reading comprehension still matters, but assignment-relevant reading should come first.

Study order should be based on relevance:

1. Study the reading concepts that directly support the end-of-week assignment first.
2. Study concepts that support learning logs but not the assignment second.
3. Skim or defer reading pieces that are not very relevant unless they are required for a quiz or the user has extra time.

This relevance order should shape the day-by-day plan.

## Core Question To Set Up

The first learning log of the week should usually begin with a Friday-assignment-centered planning question like:

> What is the best way to study this week so I can understand the readings, finish the learning logs on time, and complete the end-of-week assignment without cramming?

Adjust the wording to fit the actual week.

## Planning Principle

Do not treat readings, learning logs, and assignments as separate work streams.

Instead:

- Use the Friday assignment and the reading most relevant to it to generate the first learning log.
- Use a real confusion from the assignment, reading, or supporting class notes as the log's question/problem.
- Use examples from the assignment or project to make the reading concrete.
- Use the learning log notes as preparation for the quiz, project, or Friday assignment.
- Prefer plans where one study activity produces material for more than one deliverable.
- Revisit this week's dated class notes after each class; Wednesday notes may not exist when Monday's plan is made.

## Output Shape

When running this framework for a specific week, produce:

1. The next learning log number and due date.
2. The readings for the week, with short summaries.
3. The quiz/project/assignment due at the end of the week.
4. A reading-to-assignment relevance map.
5. A recommended guiding question for the first learning log.
6. A day-by-day study plan.
7. Two or three strategy options, with at least two concrete pros and one con for each option not chosen.
8. A recommended route forward with the first action stated plainly.
9. A first learning log entry appended to `learning log.md`.
10. A dated in-class-note relevance map and a Friday understanding session, with a specific concept and an appropriate check once those notes exist.

## Required Learning Log Entry

At the end of an initial run, add the first weekly planning entry to the running `learning log.md` file. If the user asks for a rerun without editing the log, leave it untouched and propose any alternative entries in chat.

The proposed plan is the **Insight/Answer**. Keep the question short. The **How to Learn** field should be nearly the same each week: understand the readings, understand the end-of-week deliverable, and find a small number of tasks that advance both. Do not put the week's specific plan or chosen strategy in How to Learn. In Insight/Answer, show the best path forward, the alternatives considered, and at least two concrete pros and one con for **each option not chosen**. Make the pros and cons specific to that week's deadlines, readings, and assignment. Keep each insight bullet under 20 words. Put the immediate next action in the chosen path. If a step is only planned, do not describe it as already completed. Omit unrelated account or tool incidents from the log question.

Use this format, adjusting the date, learning log number, times, and details for the actual week:

```md
## [Day] [M/D/YYYY] : Learning Log [Number]

- Question/Problem: What is my best route to Friday's assignment and this week's logs?
- When Identified: [M/D/YYYY time]
- Importance: [1-5]
- How to Learn: Understand what this week's readings cover and what Friday's deliverable requires, then find tasks that advance both.
- Insight/Answer:
    - [Unchosen option A]: pros—[specific benefit one] and [specific benefit two]; con—[specific drawback].
    - [Unchosen option B]: pros—[specific benefit one] and [specific benefit two]; con—[specific drawback].
    - Best path: [chosen route and first concrete action].
    - [How the chosen work supplies a real learning-log question or example.]
- Hours Spent Learning: [actual time or fill in]
- Minutes Spent Documenting: [actual time or fill in]
- Confidence (1-5): [actual rating or fill in]
```

The user may edit the entry later. The important requirement is that the entry preserves the actual options and tradeoffs behind the plan, with a clear next step.

## Day-By-Day Pattern

### Saturday / Sunday

- Start with the reading pieces most relevant to the end-of-week assignment.
- Do not aim for perfect understanding.
- Identify one real confusion or question.
- Build a tiny example, visual, table, or walkthrough.
- Turn that into the first learning log.

### Monday

- Make the first learning log about Friday's assignment and submit it if available.
- Check whether the end-of-week assignment is published.
- If published, read the requirements and connect them to the week's reading.
- If unpublished, brainstorm likely problem types and prepare flexible notes.
- Read Monday's class notes when available, but treat them as questions to test, not concepts already mastered.

### Tuesday

- Work on the second reading or next major concept.
- Use the assignment/project as the example source when possible.
- Capture the main confusion for the next learning log.

### Wednesday

- If Friday's assignment is unfinished or nearly finished, make the second learning log about a real question from that work. If it is substantially done, work through an unclear concept from the week's class notes and use the student's resulting insight for the log.
- Submit the second learning log if one is due and available.
- Convert the week's notes into assignment-ready understanding.
- Identify the smallest complete version of the end-of-week assignment.
- Reopen the in-class notes after Wednesday's meeting; do not infer content from an empty dated heading.

### Thursday

- Work directly on the end-of-week assignment.
- Use learning logs as notes.
- Prioritize core requirements before polish.

### Friday

- Finish and submit the assignment.
- Only polish after the required pieces are done.
- Once required work is complete, spend the remaining study time understanding the week's actual class notes. Ask the student to explain a central idea, try a small example, and identify what still feels unclear.
- Use an essay-style question if it helps reveal understanding; a trace, comparison, or short oral explanation may work better for some topics.
- If a real insight emerges, offer it as possible material for a later learning log. Do not copy notes into the log as if they were understood.

### Optional Friday Essay-Style Check

When an essay question fits the week's discussion, pose one concrete question that asks the student to explain a claim from the notes, apply it to a small example, and justify the answer. Let the student answer before giving a model explanation. Then identify what they explained correctly, one or two gaps, and a focused follow-up question or example. Use their answer, not the AI-assisted notes alone, as evidence of understanding. This is one tool for the Friday notes session, not a required weekly test.

## Strategy Options To Offer

### Option A - Reading First

Best when the user feels conceptually behind. Read first, generate questions, and let those questions become the learning logs.

### Option B - Assignment First

Best when the end-of-week assignment is already published and concrete. Read the assignment first, then go into the textbook and focus on the reading concepts that directly support the assignment's hardest requirement.

### Option C - Hybrid

Best default. Do enough reading to create useful learning logs, then use those logs to support the assignment.

## Default Recommendation

Recommend the hybrid route unless the assignment is already urgent or the user is clearly missing the underlying concepts.

## Tone And Style

Keep the plan practical and week-specific. The user wants a route forward, not a motivational essay.

Use plain language:

- "Do this first."
- "This becomes the learning log."
- "Save this example for the assignment."
- "Do not polish until the core requirement works."

The plan should feel like a study strategy that reduces duplicated work.
