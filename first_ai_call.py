import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2:latest",
        "prompt": "Explain what recursion is in one sentence",
        "stream": False
    },
    proxies={"http": None, "https": None}
)

data = response.json()
print(data["response"])