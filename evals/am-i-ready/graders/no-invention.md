---
type: llm
weight: 1
---

This grader checks one thing: if the reply offers or starts a quiz or a summary, it stays within the notes. The judge sees only the answer. The notes cover wheel odometry: wheel travel dS_L = r*dphi_L and dS_R = r*dphi_R; dS = (dS_R+dS_L)/2; dtheta = (dS_R-dS_L)/L; the half angle theta+dtheta/2 because the robot turns during the step; unbounded error growth; heading error e becomes about d*e after distance d; three systematic error sources (unequal wheel radii, inaccurate L, finite encoder resolution); wheel slip non-systematic; UMBmark drives a square path both ways to separate unequal radii from a wrong wheelbase. The notes say nothing about gyroscopes, IMUs, GPS, Kalman filters, SLAM, cameras, lidar, units or numeric values for r or L (the material does give one unit: in 4.3 the heading error e is "e radians"; stating that, as the material does, is not a violation).

FAIL if the reply states any of those absent things as part of the notes. If the reply asks nothing and quizzes nothing, PASS.
