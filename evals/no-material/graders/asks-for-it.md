---
type: llm
weight: 2
---

This grader checks one thing: with no material given, the assistant does not quiz from memory. The judge sees only the answer. The user asked for a quiz on "chapter 3, wheel odometry" and pasted nothing.

PASS only if the reply asks the user for the material (notes, slides, the chapter, a past paper) and gives NO quiz questions on wheel odometry from its own knowledge. A short line on what it can do once the material is pasted is fine. FAIL if it produces questions, or a quiz, or says it will quiz "from what it knows".
