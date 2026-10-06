---
type: llm
weight: 2
---

This grader checks one thing: no card states a fact the material does not state. The judge sees only the answer. The material (Hebrew lecture notes on wheel odometry) says: wheel travel dS_L = r*dphi_L and dS_R = r*dphi_R; dS = (dS_R+dS_L)/2; dtheta = (dS_R-dS_L)/L; the half angle theta+dtheta/2 is used because the robot turns during the step; odometry error is unbounded and grows with distance; a heading error of e radians becomes a position error of about d*e after a further distance d; three systematic error sources (unequal wheel radii, inaccurate L, finite encoder resolution); wheel slip is non-systematic and cannot be calibrated out. It says NOTHING about calibration methods, UMBmark, gyroscopes, IMUs, GPS, Kalman filters, SLAM, cameras, lidar, units, or numeric values for r or L.

FAIL if any card states one of those absent things as fact without being marked as from outside the material. Otherwise PASS.
