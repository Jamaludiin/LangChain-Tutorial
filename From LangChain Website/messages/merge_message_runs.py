import os
from langchain_groq import ChatGroq
from langchain_core.messages.utils import merge_message_runs
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
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

# Sample messages
messages = [
    SystemMessage("You're a helpful assistant."),
    HumanMessage("What is your favorite color?"),
    HumanMessage("And what is your favorite food?"),
    AIMessage("My favorite color is blue."),
    AIMessage("And I love pizza!"),
]

merged_messages = merge_message_runs(messages)

# Print the merged messages
for msg in merged_messages:
    print(f"{msg.type.capitalize()}: {msg.content}")


