---
type: llm
weight: 2
---

This grader checks one thing: the explanation starts from the material and keeps its symbols. The judge sees only the answer. For reference the material's section 4.3 says: odometry error is unbounded, each step adds error that is never removed, position error grows with distance travelled, and a heading error of e radians becomes a position error of about d * e after a further distance d.

PASS only if the explanation quotes or closely restates that passage before adding anything else, and uses the symbols e and d (not renamed) when explaining d * e. FAIL if it opens with an analogy or outside knowledge, or renames the symbols.
