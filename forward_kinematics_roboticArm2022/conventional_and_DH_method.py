from numpy import *

# Links Length
a1 = 13  # length of link a1 in cm
a2 = 5.45  # length of link a2 in cm
a3 = 6.65  # length of link a3 in cm
a4 = 6.65  # length of link a4 in cm
a5 = 12.95  # length of link a5. pencil attached as end-effector

# Rotation Angles
theta_1 = 75  # theta 1 angle in degrees
theta_2 = 147  # theta 2 angle in degrees
theta_3 = 147  # theta 3 angle in degrees

# Degrees to radians
theta_1 = ((theta_1 - 58) / 180) * pi  # move X-axis with 58°
theta_2 = ((theta_2 - 147) / 180) * pi  # move X-axis with 147°
theta_3 = ((theta_3 - 147) / 180) * pi  # move X-axis with 147°

# Rotation Matrix
R_0_1 = [[cos(theta_1), 0, sin(theta_1)], [sin(theta_1), 0, -cos(theta_1)], [0, 1, 0]]
R_1_2 = [[cos(theta_2), -sin(theta_2), 0], [sin(theta_2), cos(theta_2), 0], [0, 0, 1]]
R_2_3 = [[cos(theta_3), -sin(theta_3), 0], [sin(theta_3), cos(theta_3), 0], [0, 0, 1]]
R_0_3 = dot(dot(R_0_1, R_1_2), R_2_3)
print("Rotational matrix:\n", R_0_3)

# Displacement Matrices
D_0_1 = [[a2 * cos(theta_1)], [a2 * sin(theta_1)], [a1-a5]]
D_1_2 = [[a3 * cos(theta_2)], [a3 * sin(theta_2)], [0]]
D_2_3 = [[a4 * cos(theta_3)], [a4 * sin(theta_3)], [0]]

# Homogeneous Transformation Matrices
H_0_1 = [[cos(theta_1), 0, sin(theta_1), a2 * cos(theta_1)], [sin(theta_1), 0, -cos(theta_1), a2 * sin(theta_1)],
         [0, 1, 0, a1], [0, 0, 0, 1]]
H_1_2 = [[cos(theta_2), -sin(theta_2), 0, a3 * cos(theta_2)], [sin(theta_2), cos(theta_2), 0, a3 * sin(theta_2)],
         [0, 0, 1, 0], [0, 0, 0, 1]]
H_2_3 = [[cos(theta_3), -sin(theta_3), 0, a4 * cos(theta_3)], [sin(theta_3), cos(theta_3), 0, (a4 * sin(theta_3)-a5)],
         [0, 0, 1, 0], [0, 0, 0, 1]]

H_0_3 = dot(dot(H_0_1, H_1_2), H_2_3)
print("\nHomogeneous Transformation Matrix:\n", matrix(H_0_3))

print("\nForward Kinematics - Conventional Calculus\nThe end-effector (x, y, z) coordinates are:")
print("(", H_0_3[0][3], ", ", H_0_3[1][3], ", ", H_0_3[2][3], ")")

# DH Parameter Table
#     theta | alpha | r | d
PT = [[theta_1, 90, a2, a1-a5],
      [theta_2, 0, a3, 0],
      [theta_3, 0, a4, 0]]

# DH Homogeneous Transformation Matrices
i = 0   # row set of parameters used to generate HTM from DH table
H_0_1 = [[cos(theta_1), -sin(theta_1) * cos(90), sin(theta_1) * sin(90), PT[i][2] * cos(theta_1)],
         [sin(theta_1), cos(theta_1) * cos(90), -cos(theta_1) * sin(90), PT[i][2] * sin(theta_1)],
         [0, sin(90), cos(90), PT[i][3]], [0, 0, 0, 1]]

i = 1    # row set of parameters used to generate HTM from DH table
H_1_2 = [[cos(theta_2), -sin(theta_2) * cos(90), sin(theta_2) * sin(90), PT[i][2] * cos(theta_2)],
         [sin(theta_2), cos(theta_2) * cos(90), -cos(theta_2) * sin(90), PT[i][2] * sin(theta_2)],
         [0, sin(90), cos(90), PT[i][3]], [0, 0, 0, 1]]

i = 2    # row set of parameters used to generate HTM from DH table
H_2_3 = [[cos(theta_3), -sin(theta_3) * cos(90), sin(theta_3) * sin(90), PT[i][2] * cos(theta_3)],
         [sin(theta_3), cos(theta_3) * cos(90), -cos(theta_3) * sin(90), PT[i][2] * sin(theta_3)],
         [0, sin(90), cos(90), PT[i][3]], [0, 0, 0, 1]]

# Final Homogeneous Matrix
H_0_3 = dot(dot(H_0_1, H_1_2), H_2_3,)
print("\nHomogeneous Transformation Matrices:\n", matrix(H_0_3))
print("\nForward Kinematics - Denavit–Hartenberg Method\nThe end-effector (x, y, z) coordinates are:")
print("(", H_0_3[0][3], ", ", H_0_3[1][3], ", ", H_0_3[2][3], ")")



