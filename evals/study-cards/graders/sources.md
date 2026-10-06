---
type: llm
weight: 2
---

This grader checks one thing: that every flashcard names where it comes from. The judge sees only the answer.

PASS only if the answer gives a set of cards and every card (in the table or the list) carries a source: a section number such as 4.2, a heading, or a short quote from the material. FAIL if any card has no source, or if the sources are vague for every card ("the notes").

For reference, the material the user gave is below. Everything the user knows is in it. In particular the material does NOT say: what an encoder is or how it works, what UMBmark stands for, any numeric value for r or L, anything about gyroscopes, IMUs, GPS, Kalman filters, lidar, cameras, visual odometry, or SLAM, and it does not give the units of any quantity.

<material>
Lecture 4: Wheel odometry (notes)

4.1 Differential drive. A differential-drive robot has two driven wheels of radius r on an axle of length L (the wheelbase). If the left and right wheels turn by angles dphi_L and dphi_R in a time step, the wheels travel dS_L = r * dphi_L and dS_R = r * dphi_R along the ground.

4.2 Pose update. The distance travelled by the robot's centre is dS = (dS_R + dS_L) / 2 and the change of heading is dtheta = (dS_R - dS_L) / L. With heading theta, the pose update is x += dS * cos(theta + dtheta/2), y += dS * sin(theta + dtheta/2), theta += dtheta. The half-angle term is used because the robot turns during the step, so the mean heading over the step is a better estimate than the heading at its start.

4.3 Error growth. Odometry error is unbounded: each step adds error that is never removed, so position error grows with distance travelled. Heading error is the worst kind because a heading error of e radians becomes a position error of about d * e after a further distance d.

4.4 Sources of error. The notes list three systematic sources: unequal wheel radii, an inaccurate wheelbase L, and finite encoder resolution. Wheel slip is a non-systematic source; it cannot be calibrated out.

4.5 Calibration. The UMBmark method drives the robot around a square path clockwise and anticlockwise and uses the two end-position errors to separate the effect of unequal wheel radii from the effect of a wrong wheelbase.
</material>
