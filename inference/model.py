
# call ollama via http api
import requests

def generate(prompt: str) -> str:
    url = "http://localhost:11434/api/chat"
    headers = {
        "Content-Type": "application/json",
    }
    payload = {
        "model": "mistral",
        "messages": [{
            "role": "user",
            "content": prompt
        }],
        "stream": False
        }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

response = generate("Explain LoRA in one paragraph")
print(response)
