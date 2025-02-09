
from groq import Groq
import base64

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


groq_api_key = os.getenv('GROQ_API_KEY')


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/Users/LLM and HuggingFace/LangChain Tutorial/LangChain and Ollama/Vision_Models/PythonSets.png"


# Getting the base64 string
base64_image = encode_image(image_path)

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    model="llama-3.2-11b-vision-preview",
)

print(chat_completion.choices[0].message.content)