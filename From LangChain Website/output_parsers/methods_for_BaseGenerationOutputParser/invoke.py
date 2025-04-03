"""
8. invoke() - Run a Single Prompt Synchronously
This method runs a single prompt synchronously.
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

response = llm.invoke("What is the capital of Canada?")
print("\n=== invoke() Response ===")
print(response.content)
