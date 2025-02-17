# error 

from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the chat model
chat = ChatGroq(
    api_key=os.getenv('GROQ_API_KEY'),
    model="llama-3.3-70b-versatile"
)

# Create messages
messages = [
    HumanMessage(content="What is the capital of France?")
]

# Get response
response = chat.invoke(messages)
print("\n")
print(response.content)
print("\n")

# Add the AI's response to the message history
messages.append(response)

# Ask a follow-up question
messages.append(HumanMessage(content="What is its population?"))
response = chat.invoke(messages)
print(response.content)
print("\n")
