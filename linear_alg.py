import numpy as np

# Scalars
## Just a number
s = 2.0

# Vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

## access value
#print(a[1]) # == 5

## scalar multiplication
#print(s * a)

## addition / subtraction
# print(a + b)
# print(a - b)

## magnitude
mag = np.sqrt(np.sum(np.power(a, 2)))

## normalize
a_norm = a / mag
# print(a_norm)

# dot product
# print(np.dot(a, b))
# print(a @ b)

# cross product
# print(np.cross(a, b))
# print(np.cross(b, a))


# Matrices
M = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

# print(M.shape)

## access element
# print(M[1][2])
# print(M[1, 2])

# Identity
I = np.identity(3)
# print(I)

## Other common constructors
A = np.full((2, 2), 3.0)
# print(A)

# print(np.ones((2, 3)))
# print(np.zeros((4, 2)))


## Transpose
# print(M)
# print(M.transpose())


## Comparing matrices
A = np.array([
    [1., 2.],
    [3., 4.],
])

B = np.array([
    [2. - 1.0000000000000000000001, 2.],
    [3., 4.],
])

# print(A == B)
# print((A == B).all())

print(np.isclose(A, B))
print(np.allclose(A, B))