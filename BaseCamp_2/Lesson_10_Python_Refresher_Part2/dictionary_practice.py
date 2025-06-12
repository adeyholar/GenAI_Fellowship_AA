# Dictionary Practice for Data Organization and API Responses

# Creating a dictionary to store user data
user_data = {
    "name": "adeola",
    "age": 40,
    "city": "Chicago",
    "skills": ["Python", "Git", "Streamlit"]
}
print("Original user data:", user_data)

# Accessing values in the dictionary
print("User's name:", user_data["name"])
user_data["email"] = "adeola@outlook.com" # Adding a new key-value pair
print("Updated user data with email:", user_data)

# Updating existing values
user_data["age"] = 41
print("Age updated:", user_data["age"])

# Removing a key-value pair
del user_data["city"]
print("After removing city:", user_data)

# Simulating an API response
api_response = {
    "status": "success",
    "data": user_data,
    "message": "User profile retrieved"
} 
print("API Response:", api_response)

# Using get() method to safely access
occupation = api_response.get("data", {}).get("occupation", "Not provided")
print("Occupation:", occupation)

# Iterating over dictionary
print ("User details:")
for key, value in user_data.items():
    print(f"{key}: {value}")