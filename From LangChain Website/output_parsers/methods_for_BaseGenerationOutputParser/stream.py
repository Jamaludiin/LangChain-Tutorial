"""
13. stream() - Stream Output Synchronously
This method streams responses word by word in real time.
"""


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(model="llama-3.3-70b-versatile")

print("\n=== stream() Response ===")
for chunk in llm.stream("Tell me a short story about a robot."):
    print(chunk, end="")
