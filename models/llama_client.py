import requests

class LlamaClient:
    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: {response.text}"


# Test block
if __name__ == "__main__":
    client = LlamaClient()

    prompt = "Explain resume analysis in simple words."

    result = client.generate(prompt)

    print("\nAI Response:\n")
    print(result)