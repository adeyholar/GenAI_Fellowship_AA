import os

# Use the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'unicode_sample.txt')

# Unicode strings with international characters
text = "Hello! こんにちは! ₹500 😊"
print("Original text:", text)

# Accessing characters
print("First character:", text[0])
print("Japanese character:", text[7])  # こ
print("Rupee symbol:", text[12])  # ₹

# Length of string (counts Unicode characters)
print("Length:", len(text))

# Encoding and decoding
encoded = text.encode('utf-8')
print("UTF-8 encoded:", encoded)
decoded = encoded.decode('utf-8')
print("Decoded back:", decoded)

# Writing Unicode to a file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(text)

# Reading Unicode from a file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print("File content:", content)