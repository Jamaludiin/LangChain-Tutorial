import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages.tool import invalid_tool_call, InvalidToolCall

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Example: Creating an invalid tool call
invalid_call = invalid_tool_call(
    name="weather_tool",  # The tool name
    args="{}",  # Empty or incorrect arguments or # Missing required parameters
    id="12345",  # Optional unique ID
    error="Missing location parameter"  # Description of the error
)

# Print the invalid tool call details
print("Invalid Tool Call:", invalid_call)



"""
📌 What does invalid_tool_call do?
It creates an instance of an invalid tool call when a tool request is missing required details or has an error.
This helps to log errors and handle failures before running invalid tool requests.
"""