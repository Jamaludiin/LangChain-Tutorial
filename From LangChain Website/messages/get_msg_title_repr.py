import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages.base import get_msg_title_repr
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

# Example usage of get_msg_title_repr
title = "Hello, Groq API!"
formatted_title = get_msg_title_repr(title, bold=True)

# Print the formatted title
print(formatted_title)
