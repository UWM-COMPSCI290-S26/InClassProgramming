import numpy as np


p = np.array([0, 1, 1])
rotate_amount = np.deg2rad(45)

T1 = np.identity(3)
T1[0, 0] = np.cos(rotate_amount)
T1[0, 1] = -np.sin(rotate_amount)
T1[1, 0] = np.sin(rotate_amount)
T1[1, 1] = np.cos(rotate_amount)

T2 = np.identity(3)
T2[0, 0] = 2
T2[1, 1] = 2

T = np.matmul(T2, T1)
print(np.matmul(T, p))

# p = np.array([0, -2, 1])
# rotate_around = np.array([-2, -2])
# rotate_amount = np.deg2rad(90)
#
# T1 = np.identity(3)
# T1[0, 2] = -rotate_around[0]
# T1[1, 2] = -rotate_around[1]
#
# T2 = np.identity(3)
# T2[0, 0] = np.cos(rotate_amount)
# T2[0, 1] = -np.sin(rotate_amount)
# T2[1, 0] = np.sin(rotate_amount)
# T2[1, 1] = np.cos(rotate_amount)
#
# T3 = np.identity(3)
# T3[0, 2] = rotate_around[0]
# T3[1, 2] = rotate_around[1]
#
#
# T = np.matmul(T3, np.matmul(T2, T1))
# T = np.matmul(T3, T2, T1)

# print(np.matmul(T, p)[0:2])