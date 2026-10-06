---
type: llm
weight: 1
---

This grader checks one thing: the explanation ends with one question for the student. The judge sees only the answer. PASS if the reply contains exactly one check question addressed to the student near its end (a short closing instruction after it, such as "answer it and I'll grade it", is fine) and does not state that question's answer after asking it. The explanation before the question may well contain material the question draws on; that is not a violation. FAIL if there is no closing question, if there are several, or if the answer to the question is given right after it.
