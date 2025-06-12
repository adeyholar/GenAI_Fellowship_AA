import os

# Exception Handling with try/except/finally

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        result = None
    except TypeError:
        print("Error: Inputs must be numbers!")
        result = None
    finally:
        print("Execution of divide_numbers completed.")
    return result

# Test the function
print("Division 10 / 2:", divide_numbers(10, 2))  # Should work
print("Division 10 / 0:", divide_numbers(10, 0))  # ZeroDivisionError
print("Division '10' / 2:", divide_numbers("10", 2))  # TypeError

# Using try/except with file handling
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_file.txt')
try:
    with open(file_path, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found, creating a new one.")
    with open(file_path, 'w') as file:
        file.write("Default content.")
finally:
    print("File operation completed.")

# Verify the file
with open(file_path, 'r') as file:
    print("File content:", file.read())