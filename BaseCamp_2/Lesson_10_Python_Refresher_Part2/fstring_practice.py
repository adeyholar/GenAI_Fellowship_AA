# F-string Formatting for Dynamic Content

# Basic variables
name = "adeola"
age = 30
city = "Chicago"
current_year = 2025

# Simple F-string
greeting = f"Hello, {name}! You are {age} years old."
print("Simple F-string:", greeting)

# F-string with expression
years_until_retirement = 65 - age
retirement_message = f"{name} will retire in {years_until_retirement} years in {current_year + years_until_retirement}."
print("Retirement message:", retirement_message)

# F-string with formatting options
price = 499.95
formatted_price = f"Price: ${price:.2f}"
print("Formatted price:", formatted_price)

# F-string with multiple variables
profile = f"User: {name.upper()}, Age: {age}, Location: {city}, Year: {current_year}"
print("User profile:", profile)

# F-string with conditional logic
status = f"Status: {'Active' if age < 40 else 'Senior'}"
print("User status:", status)