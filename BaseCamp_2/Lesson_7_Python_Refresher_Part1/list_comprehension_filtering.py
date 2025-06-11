# List Comprehension with Filtering

# Original list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Basic comprehension
squares = [x**2 for x in numbers]
print("Squares of all numbers:", squares)

# Comprehension with filtering (even numbers only)
even_squares = [x**2 for x in numbers if x % 2 == 0]
print ("Squares of even numbers:", even_squares)

# Comprehension with filtering (numbers greater than 10)
large_numbers = [x for x in numbers if x > 10]
print("Numbers greater than 10:", large_numbers)

# Complex filtering (even number divisible by 4)
divisible_by_4 = [x for x in numbers if x % 2 == 0 and x % 4 == 0]
print("Even numbers divisible by 4:", divisible_by_4)