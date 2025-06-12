# String Slicing, Formatting, and Manipulation

# Original string
text = "Hello, Python Learners! こんにちは! 😊"
print("Original text:", text)

# String slicing
print("First 5 characters:", text[:5])
print("From index 7 to 12:", text[7:12])
print("Every second character:", text[::2])

# String formatting with .format()
formatted = "Name: {}, Age: {}".format("adeola", 30)
print("Formatted with .format():", formatted)

# F-string formatting
f_string = f"Welcome, {text[:6]}! You are learning at {2025}."
print("F-string:", f_string)

# Advanced manipulation
upper_text = text.upper()
print("Uppercase:", upper_text)
split_text = text.split(" ")
print("Split into words:", split_text)
joined_text = "-".join(split_text)
print("Joined with hyphens:", joined_text)

# Replacing text
replaced_text = text.replace("Python", "Programming")
print("Replaced text:", replaced_text)