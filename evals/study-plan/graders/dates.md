---
type: llm
weight: 2
---

This grader checks one thing: the plan's dates. The judge sees only the answer. For reference: today is Monday 2026-10-12 and the exam is Monday 2026-10-19, so the plan covers 2026-10-12 to 2026-10-18 (seven days: Mon 12, Tue 13, Wed 14, Thu 15, Fri 16, Sat 17, Sun 18). Sunday has no hours.

PASS only if the plan's table runs over those dates with the correct weekdays, gives Sunday 2026-10-18 no study hours (or marks it free), and the last working day before the exam (Saturday 17 or, if Sunday is used for nothing, the final planned day) contains repeats only and nothing new. FAIL on a wrong weekday, a date outside the range, or new material on the final planned day.
