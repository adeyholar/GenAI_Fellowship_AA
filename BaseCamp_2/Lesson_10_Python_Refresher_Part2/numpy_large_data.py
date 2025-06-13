import numpy as np
import time

# Creating a large array (7.5 million elements, as per session demo)
size = 7_500_000
large_array = np.arange(size)  # Array from 0 to 7,499,999
print("Large array shape:", large_array.shape)
print("First 5 elements:", large_array[:5])
print("Last 5 elements:", large_array[-5:])

# Measuring time for a simple operation (summing with Python list)
python_list = list(range(size))
start_time = time.time()
python_sum = sum([x * 2 for x in python_list])
python_time = time.time() - start_time
print(f"Python list sum time: {python_time:.2f} seconds")

# Measuring time for the same operation with NumPy
start_time = time.time()
numpy_sum = np.sum(large_array * 2)
numpy_time = time.time() - start_time
print(f"NumPy array sum time: {numpy_time:.2f} seconds")
print(f"Speedup factor: {python_time / numpy_time:.2f}x")

# Processing large data with a condition
large_evens = large_array[large_array % 2 == 0]
print("Number of even elements:", len(large_evens))
print("First 5 even elements:", large_evens[:5])