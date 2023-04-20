import math
import numpy as np

# Open File for Link Dimensions
fl = open("data1lenghts.txt", "r")
# Lengths of each link in the arm
l1 = float(fl.readline())
l2 = float(fl.readline())
l3 = float(fl.readline())
fl.close()

# Open file for joint angles and convert them it into radian

fj=open("data2angles.txt","r")

theta1 = (math.radians(float(fj.readline())))
theta2 = (math.radians(float(fj.readline())))
aux = float(fj.readline())
fj.close()
for i in range(0,6):
    theta3 = aux+float(i)

    # Define the transformation matrices for each joint
    T1 = np.array([[math.cos(theta1),0.0,math.sin(theta1),  0.0],
               [math.sin(theta1),0.0,-math.cos(theta1), 0.0],
               [0.0, 1.0, 0.0, l1],
               [0.0, 0.0, 0.0, 1.0]])

    T2 = np.array([[-math.sin(theta2), 0.0, math.cos(theta2), 0.0],
                [math.cos(theta2), 0.0, math.sin(theta2), 0.0],
               [0.0, 1.0, 0.0, 0.0],
              
               [0.0, 0.0, 0.0, 1.0]])

    T3 = np.array([[1.0, 0.0, 0.0, 0.0],
               [0.0, 1.0, 0.0, 0.0],
               [0.0, 0.0, 1.0,l2+l3+theta3 ],
               [0.0, 0.0, 0.0, 1.0]])

# Calculate the transformation matrix for the end effector
    T_end = np.dot(np.dot(T1, T2), T3)

# Extract the position of the end effector from the transformation matrix
    x = T_end[0, 3]
    y = T_end[1, 3]
    z = T_end[2, 3]
    print(np.matrix(T_end))

# Print the position of the end effector
    print("End effector position: ({}, {}, {})".format(x, y, z))
