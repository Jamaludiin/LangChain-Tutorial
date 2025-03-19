import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages.utils import convert_to_messages
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from .env
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define a sequence of messages (HumanMessage & AIMessage)
raw_messages = [
    {"type": "human", "content": "What is the capital of France?"},
    {"type": "ai", "content": "The capital of France is Paris."},
]

# Convert to list of BaseMessage objects
converted_messages = convert_to_messages(raw_messages)

# Print converted messages
for msg in converted_messages:
    print(f"{msg.type.capitalize()}: {msg.content}")

# Send user message to the LLM
response = llm.invoke(converted_messages)

# Print LLM response
print("\nAI Response:", response.content)

print("\n")

# previous no response from the AI

# Define a sequence of messages (conversation history)
raw_messages = [
    {"type": "human", "content": "What is the capital of France?"}
]

# Convert raw messages to BaseMessage objects
converted_messages = convert_to_messages(raw_messages)

# Print converted messages
for msg in converted_messages:
    print(f"{msg.type.capitalize()}: {msg.content}")

# Send the full conversation history (list[BaseMessage]) to the LLM
response = llm.invoke(converted_messages)

# Print LLM response
print("\nAI Response:", response.content)