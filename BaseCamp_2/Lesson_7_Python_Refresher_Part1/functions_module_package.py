# Demonstrating Functions, Modules, and Packages

# Function: A reusable block of code
def greet(name):
    return f"Hello, {name}!"

# Module: A single .py file with functions
print(greet("adeola"))  # Test the function

# Creating a simple module
# Save this file, then create a new file 'my_module.py' in the same folder
# Add to my_module.py:
# def farewell(name):
#     return f"Goodbye, {name}!"
# Back in this file, import and use it
import my_module  # This will work after creating my_module.py
print(my_module.farewell("adeola"))  # Test the module

# Package: A directory with __init__.py (simulated here)
# Create a folder 'my_package' in the same directory
# Inside 'my_package', create __init__.py and another file 'utils.py'
# In utils.py, add: def welcome(name): return f"Welcome, {name}!"
# Back in this file, import and use it
# from my_package.utils import welcome
# print(welcome("adeola"))  # Uncomment after creating package