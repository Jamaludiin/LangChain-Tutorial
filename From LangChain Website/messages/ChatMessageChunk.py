

import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import ChatMessageChunk, AIMessage
from dotenv import load_dotenv

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

# Simulate receiving a message chunk from AI
message_chunk = ChatMessageChunk(
    content="Hello! How can I assist you today?",
    role="ai"
)

# Print the message details
print("Message Content:", message_chunk.content)
print("Message Role:", message_chunk.role)

# Use AIMessage to represent a full AI response
ai_message = AIMessage(
    content="This is the complete AI response.",
    additional_kwargs={"source": "Groq AI"}
)

print("AI Message Content:", ai_message.content)
print("Additional Info:", ai_message.additional_kwargs)
