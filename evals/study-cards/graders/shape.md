---
type: llm
weight: 1
---

This grader checks one thing: the deliverable has the two forms a student needs. The judge sees only the answer.

PASS only if BOTH are present: (a) a table of cards with question, answer and source columns; (b) a code block for Anki with one card per line, fields separated by tabs (the answer may render tabs as wide spaces; what matters is one card per line with the question first), and a sentence telling the user to import it in Anki with the separator set to Tab. FAIL if either is missing.
