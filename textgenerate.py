import requests

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Mon nom est Mor DIOUM je suis ingénieur en informatique ",
})

print(output)