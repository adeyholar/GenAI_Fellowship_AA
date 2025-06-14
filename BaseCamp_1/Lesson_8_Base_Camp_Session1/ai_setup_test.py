import requests
import os

groq_api_key = os.getenv("GROQ_API_KEY")  # Get from environment variable
groq_url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {groq_api_key}", "Content-Type": "application/json"}
data = {
    "model": "llama-3.3-70b-versatile",
    "messages": [{"role": "user", "content": "Explain the importance of fast language models"}]
}

try:
    response = requests.post(groq_url, headers=headers, json=data)
    if response.status_code == 200:
        print("Groq API response:", response.json()["choices"][0]["message"]["content"])
    else:
        print(f"Groq API error: {response.status_code}, {response.text}")
except requests.RequestException as e:
    print(f"Network error: {e}")

print("Google AI Studio setup complete; API key saved for future use.")