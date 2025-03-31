"""
7. batch_as_completed() - Process Batch Responses as They Complete
This method returns responses as soon as they are ready.
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

prompts = ["Translate 'hello' to French", "Who painted the Mona Lisa?"]

print("\n=== batch_as_completed() Responses ===")
for response in llm.batch_as_completed(prompts):
    print(response)
