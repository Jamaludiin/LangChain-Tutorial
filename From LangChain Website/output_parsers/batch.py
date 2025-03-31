"""
6. batch() - Run Multiple Prompts Synchronously
This method runs multiple prompts synchronously.
"""


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=100,
    timeout=10,
    max_retries=2,
)

prompts = ["What is Python?", "Who discovered electricity?"]
responses = llm.batch(prompts)

print("\n=== batch() Responses ===")
for i, response in enumerate(responses):
    print(f"\nPrompt {i+1}: {prompts[i]}")
    print(f"Response: {response.content}")
