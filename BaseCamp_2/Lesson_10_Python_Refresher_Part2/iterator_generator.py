# Iterators and Generators with yield

# Regular function returning a list (memory-intensive for large data)
def generate_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(i * 2)
    return numbers

# Generator function using yield (memory-efficient)
def generate_numbers_yield(n):
    for i in range(n):
        yield i * 2

# Using the regular function
print("Using list (all in memory):")
result_list = generate_numbers(5)
print(list(result_list))  # [0, 2, 4, 6, 8]

# Using the generator
print("\nUsing generator (one at a time):")
result_generator = generate_numbers_yield(5)
for num in result_generator:
    print(num, end=" ")  # 0 2 4 6 8

# Demonstrating iterator protocol
my_iter = iter([1, 2, 3])
print("\n\nIterator next values:")
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
# print(next(my_iter))  # Raises StopIteration if uncommented