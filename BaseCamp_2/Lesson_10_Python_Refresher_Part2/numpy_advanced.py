import numpy as np

# Creating sample arrays
array1 = np.array([1, 2, 3, 4, 5, 6])
array2 = np.array([7, 8, 9, 10, 11, 12])

# Reshaping arrays
reshaped1 = array1.reshape(2, 3)  # 1D to 2D (2x3)
print("Reshaped array 1:\n", reshaped1)

reshaped2 = array2[:6].reshape(2, 3)  # Take first 6 elements, reshape to 2x3
print("Reshaped array 2:\n", reshaped2)

# Concatenation (vertical stacking)
concatenated_v = np.vstack((reshaped1, reshaped2))
print("Vertical concatenation:\n", concatenated_v)

# Concatenation (horizontal stacking) - adjust for compatibility
concatenated_h = np.hstack((reshaped1, reshaped2))
print("Horizontal concatenation:\n", concatenated_h)

# Mathematical operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Element-wise addition
addition = matrix1 + matrix2
print("Element-wise addition:\n", addition)

# Matrix multiplication
multiplication = np.dot(matrix1, matrix2)
print("Matrix multiplication:\n", multiplication)

# Element-wise square root
sqrt_matrix = np.sqrt(matrix1)
print("Element-wise square root:\n", sqrt_matrix)