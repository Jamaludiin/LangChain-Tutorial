import os
from dotenv import load_dotenv
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.messages.modifier import RemoveMessage

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Sample conversation messages
messages = [
    SystemMessage(content="You are an AI assistant."),
    HumanMessage(content="Hello, how are you?", id="msg-100"),
    AIMessage(content="I'm doing great! How can I assist you today?", id="msg-101"),
    RemoveMessage(id="msg-101")  # Request to remove the AI response
]

# ✅ Solution: Remove `RemoveMessage` before sending to Groq
filtered_messages = [msg for msg in messages if not isinstance(msg, RemoveMessage)]

# Generate response using Groq API
response = llm.invoke(filtered_messages)

# Print the AI response
print(response.content)
