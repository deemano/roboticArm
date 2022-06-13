from numpy import *

# Link lengths
a1 = 13 # 12.9  # length of link a1 in cm
a2 = 5.1 # 5.1  # length of link a2 in cm
a3 = 6.65 # 6.7  # length of link a3 in cm
a4 = 6.55 # 6.5  # length of link a4 in cm
a5 = 4.9 # 4.9  # length of link a5 in cm

# Angles
theta_1 = 240  # theta 1 angle in degrees
theta_2 = 200  # theta 2 angle in degrees
theta_3 = 120  # theta 3 angle in degrees
# Degrees to radians
#theta_1 = (theta_1 / 180) * pi  # theta 1 in radians
#theta_2 = (theta_2 / 180) * pi  # theta 2 in radians
#theta_3 = (theta_3 / 180) * pi  # theta 3 in radians

# Rotation Matrix
R_0_1 = [[cos(theta_1), 0, sin(theta_1)], [sin(theta_1), 0, -cos(theta_1)], [0, 1, 0]]
R_1_2 = [[cos(theta_2), -sin(theta_2), 0], [sin(theta_2), cos(theta_2), 0], [0, 0, 1]]
R_2_3 = [[cos(theta_3), -sin(theta_3), 0], [sin(theta_3), cos(theta_3), 0], [0, 0, 1]]

R_0_3 = dot(R_2_3, dot(R_0_1, R_1_2))
print("Rotational matrix:\n", R_0_3)

# Displacement Matrices
D_0_1 = [[a2 * cos(theta_1)], [a2 * sin(theta_1)], [a1]]
D_1_2 = [[a3 * cos(theta_2)], [a3 * sin(theta_2)], [0]]
D_2_3 = [[a4 * cos(theta_3)], [a4 * sin(theta_3)], [a5]]

# Homogeneous Transformation Matrices
H_0_1 = [[cos(theta_1), 0, sin(theta_1), a2 * cos(theta_1)], [sin(theta_1), 0, -cos(theta_1), a2 * sin(theta_1)],
         [0, 1, 0, a1], [0, 1, 0, a1]]
H_1_2 = [[cos(theta_2), -sin(theta_2), 0, a3 * cos(theta_2)], [sin(theta_2), cos(theta_2), 0, a3 * sin(theta_2)],
         [0, 0, 1, 0], [0, 0, 0, 1]]
H_2_3 = [[cos(theta_3), -sin(theta_3), 0, a4 * cos(theta_3)], [sin(theta_3), cos(theta_3), 0, a4 * sin(theta_3)],
         [0, 0, 1, a5], [0, 0, 0, 1]]

H_0_3 = dot(H_2_3, dot(H_1_2, H_2_3))
print("\nHomogeneous Transformation Matrix:\n", H_0_3)

print("\nForward Kinematics:\nBy using the Displacement & Rotation matrices we get end-effector (x, y, z) coordinates: \n(", -H_0_3[0][3], ", ", -H_0_3[1][3], ", ", H_0_3[2][3], ")")
