

import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import ChatMessage, AIMessage
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

# Define a multi-turn conversation
conversation = [
    ChatMessage(role="system", content="You are a helpful AI that assists with coding."),
    ChatMessage(role="user", content="What is the benefit of AI in software development?"),
]

# Send only the latest user message to the model
response = llm.invoke(conversation[-1].content)

# Store AI response as a ChatMessage
ai_response = ChatMessage(role="assistant", content=response.content)

# Add AI response to the conversation history
conversation.append(ai_response)

# Print each message in the conversation
print("\n📌 Conversation History:")
for msg in conversation:
    print(f"{msg.role.capitalize()}: {msg.content}")

# Show all attributes of a ChatMessage object
print("\n🔹 ChatMessage Object Details:")
print(ai_response.__dict__)  # Print all supported attributes
