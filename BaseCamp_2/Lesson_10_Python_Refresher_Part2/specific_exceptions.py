import os

# Function to process user input with specific exception handling
def process_input(value, divisor):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'result.txt')
    print(f"File will be created at: {file_path}")  # Debug print
    try:
        number = float(value)  # Convert to float, may raise ValueError
        result = number / divisor  # May raise ZeroDivisionError
        with open(file_path, 'w') as file:
            file.write(f"Result: {result}")
    except ValueError:
        print("ValueError: Please enter a valid number!")
    except ZeroDivisionError:
        print("ZeroDivisionError: Division by zero is not allowed!")
    except FileNotFoundError:
        print("FileNotFoundError: Could not access the file system!")
    except PermissionError:
        print("PermissionError: Insufficient permissions to write the file!")
    finally:
        print("Operation completed, checking file...")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                print("File content:", file.read())
        else:
            print("No file created due to error.")

# Test cases
print("Test 1: Valid input")
process_input("10", 2)  # Should work
print("\nTest 2: Zero division")
process_input("10", 0)  # ZeroDivisionError
print("\nTest 3: Invalid input")
process_input("abc", 2)  # ValueError
print("\nTest 4: Simulate permission issue (uncomment to test)")
# process_input("5", 1)  # Uncomment to test PermissionError (requires restricted dir)

# Verify file existence
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result.txt')
if os.path.exists(file_path):
    os.remove(file_path)  # Clean up
    print("Test file removed.")