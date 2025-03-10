from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


groq_api_key = os.getenv('GROQ_API_KEY')


client = Groq()
completion = client.chat.completions.create(
    model="llama-3.2-11b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f2/LPU-v1-die.jpg"
                    }
                }
            ]
        }
    ],
    temperature=1,
    #max_completion_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print("\n")
print(completion.choices[0].message)
print("\n")
print(completion.choices[0].message.content)
print("\n")

