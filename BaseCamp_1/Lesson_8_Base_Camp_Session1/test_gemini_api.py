import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print("API Key Loaded:", bool(api_key))  # Debug: Confirm key is loaded

# Configure the Gemini API
try:
    genai.configure(api_key=api_key)
    print("API Configured Successfully")
except Exception as e:
    print("Configuration Error:", str(e))

# Create a model instance
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Make a test API call with a directive prompt
try:
    prompt = (
        "You are the Google Gemini API. I am testing your functionality with a valid API key. "
        "Do not provide any explanations or request additional information. "
        "Respond exactly with the following text: 'Your API key is working successfully.'"
    )
    response = model.generate_content(prompt)
    print("Full Response:", response)  # Debug: Inspect response object
    print("Response Text:", response.text)
except Exception as e:
    print("API Call Error:", str(e))