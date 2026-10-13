---
type: llm
weight: 1
---

This grader checks one thing: the answer gives exactly one concrete next step tied to the material (a passage to reread, named by section or quote, or one habit to change). The judge sees only the answer. It may appear anywhere in the reply (the model answer may follow it). The reply also ends with a closing line starting "Next:" that may repeat this step and name words to type afterwards (for example: import the card, reread the passage, then say *quiz me on this*); that closing line is the same step plus a pointer, not a second next step, and flashcards built from the missed points are not next steps either. PASS if there is one such next step; FAIL if there is none, or if the reply gives a list of several separate next steps.
