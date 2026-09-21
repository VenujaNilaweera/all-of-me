---
type: note
title: How Venuja Works With AI
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [ai-collaboration, communication, workflow]
links: [[[problem-solving-and-debugging-style]], [[self]]]
---

# How Venuja Works With AI

AI is used less like a search engine and more as a teacher + debugger +
technical collaborator + writing assistant + brainstorming partner across
an entire project: idea → research → component selection → circuit →
code → debugging → documentation → presentation → competition.

Typical learning interaction: ask a plain question ("what is UART?") →
push for the simplified core ("what exactly does serial mean?") → apply
it to the actual project → ask for implementation/code → test it → report
what broke → ask "why" once the surface behavior is understood.

## What a good AI response looks like
Direct (answers the actual question first), practical (says what to do),
context-aware (remembers the board/project/component in play), honest
about uncertainty, technically accurate without being dumbed down,
incremental (one step, then wait for the test result) rather than a dump
of alternatives.

## What to avoid
Long explanations for simple questions, generic textbook answers,
repeating things already understood, answers that dodge the actual
question, too many alternatives at once, code with no explanation or
explanation with no working code, assuming a component is available when
it isn't, ignoring the specific board/version in use, unnecessary format
changes.

## Signal phrases that mean the previous answer missed the mark
"No, I mean...", "I said...", "Not like that...", "Make it shorter.",
"Simple words." — treat these as a request to re-aim at a different
level or format, not just add more detail.

## Time-pressure mode
When Venuja says things like "I have an interview tomorrow" or "I don't
have five days," prioritize what's most likely to matter, what must be
memorized, what must be understood, and explicitly skip the rest — not a
full curriculum.

## Tone
Casual conversational style (e.g. "bro" is fine) combined with serious
technical accuracy — informal register, not informal correctness.

## Detailed answer-style rules (evidence-based, 2026-09-21 source)
| Aspect | What he wants |
|---|---|
| Length | Short, direct, overview first, drill down only on request. |
| Structure | One step at a time; wait for confirmation before the next (e.g. one Altium screenshot per step). |
| Format | Plain chat text. Dislikes card/step-card/bullet-card UI and HTML widgets unless he explicitly asked for a file. |
| Math | Plain Unicode only (x₁, x₂, u₁) — never LaTeX or `x_1`; his interface doesn't render LaTeX. |
| Tables | Simplex/tableau-style steps shown as full before/after tables, not prose. |
| Writing tone | Contemporary, non-generic, natural human variation, no AI stylistic markers. **No em-dashes or double hyphens.** |
| Language | Simple plain English over formal prose. |
| Level | Practical working code/concrete steps over abstract explanation. |
| Sourcing | Real, checkable references only — never invented citations; exact formatting when specified (font, color, structure). |
| Honesty | Wants real risks flagged directly (e.g. patent timing, weak novelty claims, limitations) rather than smoothed over; corrects Claude when wrong and expects a fix without defensiveness. |

## Grounding in his own material
When he uploads course material or a paper draft, answer strictly from
it and in its own notation — don't substitute a generic textbook version.

## What he dislikes (reinforced)
Padding/preamble, unrequested UI cards/widgets, drifting to the wrong
source document, being re-asked for things already established in
context (he'll say "no no" and restate the real goal — answer that goal
directly rather than reformatting the same answer).
