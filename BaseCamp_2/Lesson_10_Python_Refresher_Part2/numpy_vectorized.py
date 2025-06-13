import numpy as np
import time

# Creating a large array
size = 7_500_000
large_array = np.arange(size)

# Vectorized operation: Square each element
start_time = time.time()
squared_array = large_array ** 2
vectorized_time = time.time() - start_time
print("Vectorized squaring time:", vectorized_time, "seconds")
print("First 5 squared elements:", squared_array[:5])

# Python loop equivalent (non-vectorized)
python_list = list(range(size))
start_time = time.time()
squared_list = [x ** 2 for x in python_list]
python_time = time.time() - start_time
print("Python loop squaring time:", python_time, "seconds")
print("First 5 squared elements (Python):", squared_list[:5])

# Vectorized operation: Element-wise addition
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
result = array1 + array2
print("Vectorized addition:", result)

# Comparing with a loop
loop_result = [a + b for a, b in zip(array1, array2)]
print("Loop addition:", loop_result) 