---
type: llm
weight: 2
---

This grader checks one thing: the answers are withheld. The judge sees only the assistant's reply to a request for a quiz.

PASS only if the reply gives numbered questions and does NOT give their answers, model answers or an answer key in the same reply (a sentence saying the key comes after the user answers is expected). FAIL if any question is followed by its answer, or an answer key appears anywhere in the reply.
