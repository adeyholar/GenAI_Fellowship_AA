import os

# Use the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'sample.txt')

# Writing to a file
with open(file_path, 'w') as file:
    file.write("Hello, this is a test file!\n")
    file.write("Line 2: Learning file handling.\n")

# Reading from a file
with open(file_path, 'r') as file:
    content = file.read()
    print("File content:")
    print(content)

# Appending to a file
with open(file_path, 'a') as file:
    file.write("Line 3: Appended text.\n")

# Reading line by line
with open(file_path, 'r') as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())