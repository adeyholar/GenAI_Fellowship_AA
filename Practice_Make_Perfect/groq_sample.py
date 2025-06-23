import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file import Groq
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
print("API KEY loaded:", bool(api_key))

#Configure the Groq API client
try:
    client = Groq(api_key=api_key)
    print("Groq client configured successfully.")
except Exception as e:
    print("Error configuring Groq client:", str(e))

# Make a simple API call to test the client
try:
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello, Groq! Confirm that the API is working."}],
        model="llama3-8b-8192"
    )
    print("Response Text:", chat_completion.choices[0].message.content)
except Exception as e:
    print("Error making API call:", str(e))