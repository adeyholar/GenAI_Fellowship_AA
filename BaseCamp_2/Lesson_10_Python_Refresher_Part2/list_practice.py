# Dynamic Lists Practice

# Basic list and slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)
print("First 5 elements:", numbers[:5])
print("Last 3 elements:", numbers[-3:])
print("Every second element:", numbers[::2])

# List comprehension
squares = [x**2 for x in numbers]
print("Squares:", squares)

# Nested lists Operations
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print("Flattened nested list:", flattened)