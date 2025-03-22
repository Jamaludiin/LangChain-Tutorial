import os
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=1000,
    timeout=10,
    max_retries=2,
)

# Define a simple calculator tool
@tool
def calculator(operation: str, num1: float, num2: float) -> float:
    """Performs basic arithmetic operations (add, subtract, multiply, divide)."""
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Use add, subtract, multiply, or divide.")

# Bind tools to the model
llm_with_tools = llm.bind_tools([calculator])

# Define the chain to extract arguments and call the tool
chain = llm_with_tools | (lambda msg: msg.tool_calls[0]["args"]) | calculator

# Error handling wrapper
def try_except_tool(tool_args: dict, config: RunnableConfig):
    """Attempts to call the tool and catches errors."""
    try:
        return calculator.invoke(tool_args, config=config)
    except Exception as e:
        return f"Error: {e}"

# Update chain with error handling
chain = llm_with_tools | (lambda msg: msg.tool_calls[0]["args"]) | try_except_tool

# Run the chain with test cases
print(chain.invoke("Calculate: 10 divided by 2"))   # 5.0
print(chain.invoke("Calculate: 5 plus 3"))         # 8
print(chain.invoke("Calculate: 10 divided by 0"))  # Error: Cannot divide by zero
print(chain.invoke("Calculate: 4 to the power of 2"))  # Error: Invalid operation
