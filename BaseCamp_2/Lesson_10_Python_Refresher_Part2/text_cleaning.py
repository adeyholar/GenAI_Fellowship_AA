import os

# Text Processing and Cleaning

# Raw text with noise
raw_text = "  Hello, World!  @user #python   123   \n\tExtra   Spaces   😊  "
print("Raw text:", raw_text)

# Basic cleaning: strip whitespace
cleaned_text = raw_text.strip()
print("Stripped text:", cleaned_text)

# Remove special characters and digits
cleaned_text = ''.join(char for char in cleaned_text if char.isalpha() or char.isspace())
print("Removed special chars/digits:", cleaned_text)

# Convert to lowercase
cleaned_text = cleaned_text.lower()
print("Lowercase text:", cleaned_text)

# Split into words and remove empty strings
words = [word for word in cleaned_text.split() if word]
print("Cleaned words:", words)

# Join with single spaces
cleaned_sentence = " ".join(words)
print("Cleaned sentence:", cleaned_sentence)

# Writing cleaned data to a file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'cleaned_text.txt')
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(cleaned_sentence)

# Reading back to verify
with open(file_path, 'r', encoding='utf-8') as file:
    verified_content = file.read()
    print("Verified content from file:", verified_content)