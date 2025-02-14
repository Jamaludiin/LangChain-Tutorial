import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Create a user message
user_message = HumanMessage(
    content="What is the capital of France?"
)

# Send the message and get AI response
response = llm.invoke([user_message])

# Print AI response
print(response)
