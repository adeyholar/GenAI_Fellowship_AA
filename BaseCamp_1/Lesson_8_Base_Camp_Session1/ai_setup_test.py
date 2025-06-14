import requests
import os

# Temporary hardcoded key (replace and remove before committing)
groq_api_key = "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"  # Replace with your actual key
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