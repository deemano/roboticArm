from numpy import *

# Link lengths
a1 = 13 # length of link a1 in cm
a2 = 5.1  # length of link a2 in cm
a3 = 6.65  # length of link a3 in cm
a4 = 6.55  # length of link a4 in cm
a5 = 4.9  # length of link a5 in cm
# a6 = 0  # length of link a6 in cm

# Angles
theta_1 = 240  # theta 1 angle in degrees
theta_2 = 200  # theta 2 angle in degrees
theta_3 = 120  # theta 3 angle in degrees

alpha_1 = 90    # first alpha angle
# Rotation Matrix
R_0_1 = [[cos(theta_1), 0, sin(theta_1)], [sin(theta_1), 0, -cos(theta_1)], [0, 1, 0]]
R_1_2 = [[cos(theta_2), -sin(theta_2), 0], [sin(theta_2), cos(theta_2), 0], [0, 0, 1]]
R_2_3 = [[cos(theta_3), -sin(theta_3), 0], [sin(theta_3), cos(theta_3), 0], [0, 0, 1]]
R_0_3 = dot(R_2_3, dot(R_0_1, R_1_2))
print("Rotational matrix:", R_0_3)

theta_1 = (theta_1 / 180) * pi  # theta 1 in radians
theta_2 = (theta_2 / 180) * pi  # theta 2 in radians
theta_3 = (theta_3 / 180) * pi  # theta 3 in radians
alpha_1 = (alpha_1 / 180) * pi # alpha 1 in radians

# DH Parameter Table for 3 DOF Planar
#     theta | alpha | r | d
PT = [[theta_1, alpha_1, a2, a1],
      [theta_2, 0, a3, 0],
      [theta_3, 0, a4, a5]]

# Homogeneous Transformation Matrices
i = 0
H_0_1 = [[cos(theta_1), -sin(theta_1) * cos(PT[i][1]), sin(theta_1) * sin(PT[i][1]), PT[i][2] * cos(theta_1)],
         [sin(theta_1), cos(theta_1) * cos(PT[i][1]), -cos(theta_1) * sin(PT[i][1]), PT[i][2] * sin(theta_1)],
         [0, sin(PT[i][1]), cos(PT[i][1]), PT[i][3]], [0, 0, 0, 1]]

i = 1
H_1_2 = [[cos(theta_2), -sin(theta_2) * cos(PT[i][1]), sin(theta_2) * sin(PT[i][1]), PT[i][2] * cos(theta_2)],
         [sin(theta_2), cos(theta_2) * cos(PT[i][1]), -cos(theta_2) * sin(PT[i][1]), PT[i][2] * sin(theta_2)],
         [0, sin(PT[i][1]), cos(PT[i][1]), PT[i][3]], [0, 0, 0, 1]]

i = 2
H_2_3 = [[cos(theta_3), -sin(theta_3) * cos(PT[i][1]), sin(theta_3) * sin(PT[i][1]), PT[i][2] * cos(theta_3)],
         [sin(theta_3), cos(theta_3) * cos(PT[i][1]), -cos(theta_3) * sin(PT[i][1]), PT[i][2] * sin(theta_3)],
         [0, sin(PT[i][1]), cos(PT[i][1]), PT[i][3]], [0, 0, 0, 1]]

# Final Homogeneous Matrix
H_0_2 = dot(H_0_1, H_1_2)
H_0_3 = dot(H_0_2, H_2_3)
print("\nHomogeneous coordinates:", matrix(H_0_3))
print("\nForward Kinematics:\nBy using the Denavit–Hartenberg parameters, we get tnd-effector (x, y, z) coordinates: \n(", H_0_3[0][3] - a4-.38, ", ", H_0_3[1][3], ", ", H_0_3[2][3], ")")
