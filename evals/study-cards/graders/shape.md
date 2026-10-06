---
type: llm
weight: 1
---

This grader checks one thing: the deliverable has the two forms a student needs. The judge sees only the answer.

PASS only if BOTH are present: (a) a table of cards with question, answer and source columns; (b) a code block for Anki with one card per line, fields separated by tabs (the judge may see a tab as a wide gap; what matters is one card per line, question first, with a clear field break), and a sentence telling the user to import it in Anki with the separator set to Tab. A cloze card, if any, must be in a separate block for the Cloze note type, not mixed into the basic block. FAIL if either is missing.
