# Basic File Handling in Python

# Writing to a file
with open('sample.txt', 'w') as file:
    file.write("Hello, this is a test file!\n")
    file.write("Line 2: Learning file handling.\n")

# Reading from a file
with open('sample.txt', 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# Appending to a file
with open('sample.txt', 'a') as file:
    file.write("Line 3: Appended text.\n")

# Reading line by line
with open('sample.txt', 'r') as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())