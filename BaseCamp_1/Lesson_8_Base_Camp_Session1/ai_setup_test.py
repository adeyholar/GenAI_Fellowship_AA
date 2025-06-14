from dotenv import load_dotenv
import requests
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    print("Error: GROQ_API_KEY not found in .env file. Check your .env file.")
else:
    groq_url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {groq_api_key}", "Content-Type": "application/json"}
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": "Explain the importance of fast language models in network diagnostics"}]
    }

    try:
        response = requests.post(groq_url, headers=headers, json=data)
        if response.status_code == 200:
            print("Groq API response:", response.json()["choices"][0]["message"]["content"])
        else:
            print(f"Groq API error: {response.status_code}, {response.text}")
    except requests.RequestException as e:
        print(f"Network error: {e}")

device_status = {"Router1": "Up", "Switch1": "Down", "Router3": "Up"}
print("Network Device Status:", device_status)

print("Google AI Studio setup complete; API key saved for future use.")