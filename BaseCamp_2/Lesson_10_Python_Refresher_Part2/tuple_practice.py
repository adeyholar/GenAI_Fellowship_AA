# Tuple Practice for Immutable Data and Packing/Unpacking

# Creating tuples (immutable)
user_info = ("adeola", 30, "Chicago")
print("Original tuple:", user_info)

# Attempting to modify (will raise an error if uncommented)
# user_info[0] = "new_name"  # This would fail due to immutability

# Packing and unpacking
name, age, city = user_info  # Unpacking
print("Unpacked - Name:", name, "Age:", age, "City:", city)

# Using tuples with multiple assignments
point = (3, 4)
x, y = point
print("Point coordinates - X:", x, "Y:", y)

# Tuple with mixed types and nesting
mixed_tuple = (1, "hello", (2.5, 3.5))
print("Mixed tuple:", mixed_tuple)
nested_x, nested_y = mixed_tuple[2]
print("Nested values - X:", nested_x, "Y:", nested_y)

# Using tuples in a function
def get_person_details():
    return "adeola", 30, "Chicago"

person_name, person_age, person_city = get_person_details()
print("Function return - Name:", person_name, "Age:", person_age, "City:", person_city)