---
type: llm
weight: 2
---

This grader checks one thing: the grade matches the material. The judge sees only the answer. For reference: the user's answer made three claims. (1) The half angle is used because the robot turns during the step, so the mid-step heading is used: this is RIGHT (section 4.2 says exactly this). (2) Heading error is worse because wheels slip more when turning: this is WRONG; the material says heading error is worse because a heading error of e radians becomes a position error of about d*e after a further distance d, and says nothing about slip when turning. (3) The error can be fixed later by a Kalman filter: the material says nothing about Kalman filters; it says odometry error is never removed.

PASS only if ALL hold: claim (1) is marked right; claim (2) is marked wrong (or not supported) AND the d*e reason from the material is given as what the notes actually say; claim (3) is not marked right (it may be marked wrong, unsupported, or "cannot confirm from your material"). FAIL otherwise.
