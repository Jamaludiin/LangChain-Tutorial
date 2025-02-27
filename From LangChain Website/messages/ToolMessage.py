# This example assumes you're calling a multiplication tool and sending the result back to the model using ToolMessage.

import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import ToolMessage
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

# Simulating a tool that multiplies two numbers
def multiply(a: int, b: int) -> int:
    return a * b

# Simulated tool call request
tool_call_id = "call_123456"
input_data = {"a": 5, "b": 5}

# Execute the tool
result = multiply(**input_data)

# Create a ToolMessage to send the result back to the model
tool_message = ToolMessage(
    content=str(result),  # Sending the result (42) as a string
    tool_call_id=tool_call_id
)

# Print the tool message for debugging
print(tool_message)

print(tool_message.content)

