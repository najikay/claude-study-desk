---
name: study-cards
description: "Turn notes, slides, a chapter or a past paper into flashcards, each with its question, answer and the passage it comes from, as a table and as a block ready to paste into Anki. Use when the user shares study material and says \"make flashcards\", \"cards for this chapter\", \"help me memorise this\" or \"turn my notes into Anki cards\". Not for a summary of the material, and not for material the user has not provided (it will not work from memory of a textbook)."
---

# Flashcards

Input: the material (notes, slides pasted as text, a chapter, a past paper, a formula sheet) and, if given, what the student wants covered and how many cards. With no count, make one card per distinct fact, rule, definition or step, usually 15 to 40 for a chapter; say how many you made and offer more or fewer.

## The rule of this desk
**Every question comes from the material.** Each card, question, model answer and grade points to the passage it came from: quote its words or name its section. Nothing from outside the material enters unmarked: where you add a fact, a definition, an example or an analogy the material does not contain, label it `from outside the material:` so the student can tell what the course said from what you said. Do not guess what the material "probably" says; where a passage is missing or cut off, say so. Keep the material's own terms, symbols, numbers, dates and names; do not correct the material silently, and if you think it is wrong, say so separately and mark that as your own view. A wrong answer is called wrong, with the passage that shows it; do not soften it, and do not call a partial answer complete. If the student gives no material, say so and ask for it: notes, slides pasted as text, a chapter, a past paper. Do not work from memory of a textbook you were not given.

## Your own commentary
What you say in your own voice follows the same honesty: say what the material says, word an inference as an inference ("my reading is"), and do not state how an exam will be set, what an examiner wants, or what the student's grade will be. Answer in the language of the material unless the student asks for another; a card or question in Hebrew or Arabic keeps the material's terms as written.

## Care
Write to the student as "you". Do not guess their level, age or course from their name or their language; ask when it matters. A wrong answer is a fact about the answer, not about the student: no "obviously", no "you should know this". Never put the student's material into a web search.

## How to write a card
- **One fact per card.** A card that asks two things is two cards.
- **The question states its context** ("In the EKF update step, what is the Kalman gain multiplied by?"), so the card makes sense on its own a week later.
- **Prefer recall over recognition**: no yes/no questions, no multiple choice. For a definition, make two cards: term → meaning and meaning → term. For a list of steps or parts, one card per item with its position ("Step 3 of the handshake is…"), plus one card for the count.
- **Cloze where the material has a key sentence**: `The Kalman gain weights the {{c1::innovation}} against the {{c2::prior}}.`
- **Numbers, dates, formulas and names exactly as the material gives them.** A formula card asks for the formula; a symbol card asks what a symbol stands for.
- **Cover the material evenly**: not twenty cards on page one and none on the last section. If the student named a focus, follow it and say what you left out.
- **Skip what cannot be a card**: the author's opinions, worked examples (those become quiz questions, not cards), and anything the material only mentions in passing without stating.

## Output, in this order
1. One line: what the cards cover and how many there are.
2. **The table**: `#` · `question` · `answer` · `source` (the section, page or heading, with a short quote when a number or definition is at stake).
3. **The Anki block**: a code block, one card per line, `question<TAB>answer<TAB>source` (a cloze card goes on one line with its answer field empty). Say: in Anki, File → Import, set the field separator to Tab, and allow HTML if the material has formulas. Nothing else in the block.
4. **What the material does not say** that the student may expect a card on (a term used but never defined, a step named but not explained), so they know where the notes are thin. Do not fill those gaps yourself.

## Notes
- A card the student marks as "too easy" or "too hard" is theirs to drop: offer to regenerate, do not argue.
- Formulas: write them as the material does (LaTeX if the material is LaTeX, plain text otherwise). Do not simplify or rearrange.
