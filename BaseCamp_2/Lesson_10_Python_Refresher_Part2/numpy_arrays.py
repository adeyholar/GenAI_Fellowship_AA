import numpy as np

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Creating a 2D array (matrix)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

# Creating a 3D array
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", array_3d)

# Array properties
print("Shape of 2D array:", array_2d.shape)  # (2, 3)
print("Size of 3D array:", array_3d.size)    # 8
print("Data type:", array_2d.dtype)          # int32 or int64

# Manipulating arrays
array_2d[0, 1] = 10  # Modify an element
print("Modified 2D Array:\n", array_2d)

# Reshaping an array
reshaped = array_1d.reshape(1, 5)
print("Reshaped 1D to 2D:\n", reshaped)