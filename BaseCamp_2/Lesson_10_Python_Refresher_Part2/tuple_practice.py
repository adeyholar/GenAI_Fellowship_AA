# Tuple Practice for Immutable Data and Packing/Unpacking

# Creating tupples (immutable)
user_info = ("adeola", 30, "Chicaago")
print ("Original tuple:", user_info)

# Attempting to modify (will raise an error if uncommented)
# user.info[0] = "name_name" # This would fail due to immutability

# Packing and unpacking
name, age, city = user_info # Unpacking
print ("Unpacked - Name:", name, ", Age:", age, ", City:", city)

# Using tuples with multiple assignments
proint = (3, 4)
x, y = proint
print("Point coordinates - x:", x, ", y:", y)

# Tuple with mixed types and nesting
mixed_tuple = (1, "hello", (2.5, 3,5))
print("Mixed tuple:", mixed_tuple)
nested_x, nested_y = mixed_tuple[2]  # Unpacking nested tuple
print("Nested tuple values - x:", nested_x, ", y:", nested_y)

# Using tuples in functions
def get_person_details():
    return ("adeola", 40, "Chicago")

person_name, person_age, person_city = get_person_details()
print("Function returned - Name:", person_name, ", Age:", person_age, ", City:", person_city)