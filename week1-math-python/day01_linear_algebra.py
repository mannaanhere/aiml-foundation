import numpy as np

# ===== SCALARS =====
a = 5
b = 3
print("Scalar Addition:", a + b)
print("Scalar Multiplication:", a * b)

# ===== VECTORS =====
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("\nVector v1:", v1)
print("Vector v2:", v2)

# Vector Addition
print("v1 + v2:", v1 + v2)

# Dot Product
dot_product = np.dot(v1, v2)
print("Dot Product:", dot_product)

# ===== MATRICES =====
M1 = np.array([[1, 2],
               [3, 4]])

M2 = np.array([[5, 6],
               [7, 8]])

print("\nMatrix M1:\n", M1)
print("Matrix M2:\n", M2)

# Matrix Addition
print("M1 + M2:\n", M1 + M2)

# Matrix Multiplication
print("M1 x M2:\n", np.matmul(M1, M2))

# ===== TRANSPOSE =====
print("\nTranspose of M1:\n", M1.T)