import os
import json
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq API key
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define a tool using the @tool decorator
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

# Bind the tool to the model
model_with_tools = llm.bind_tools([multiply])

# User input
user_input = "What is 5 multiplied by 6?"

# Invoke the model
response = model_with_tools.invoke(user_input)

print(response, "\n")

# Check if the model made a tool call
if response.tool_calls:
    for tool_call in response.tool_calls:
        if tool_call["name"] == "multiply":
            args = tool_call["args"]  # Extract arguments
            # Manually execute the tool
            result = multiply.invoke(args)  # Correct way to call the tool 
            print(f"Multiplication Result: {result}")
else:
    print(response.content)  # Print normal response if no tool call
