from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
import requests
from IPython.display import Audio

API_URL = "https://api-inference.huggingface.co/models/myshell-ai/MeloTTS-French"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

audio_bytes = query({
	"inputs": "The answer to the universe is 42",
})
# You can access the audio with IPython.display for example


if audio_bytes:
# Save the audio to a file
	file_path = 'output_audio.wav'
	with open(file_path, 'wb') as audio_file:
    	 audio_file.write(audio_bytes)
    # Load and display the audio for IPython environments
	Audio(file_path)
else:
	 print("Failed to generate audio.")