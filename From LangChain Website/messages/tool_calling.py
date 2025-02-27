import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Define simple math tools
@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b

# List of tools
tools = [add, multiply]

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Bind tools to the LLM
llm_with_tools = llm.bind_tools(tools)

# Query that requires tool calls
query = "What is 5 + 5? Also, what is 5 * 5?"

# Invoke the model and get tool calls
response = llm_with_tools.invoke(query)

# Print the tool calls
print(response.tool_calls)

# Extract tool calls
tool_calls = response.tool_calls

# Execute tool calls using .invoke()
results = {}
for tool_call in tool_calls:
    tool_name = tool_call["name"]
    args = tool_call["args"]

    if tool_name == "add":
        results[tool_call["id"]] = add.invoke(args)  # Fix: use .invoke()
    elif tool_name == "multiply":
        results[tool_call["id"]] = multiply.invoke(args)  # Fix: use .invoke()

# Print the final results
print("Final Results:", results)


print("also like this\n")

print("Final Results:", results.values())
print("also like this\n")

# Print results in a single row format
print(" ".join(map(str, results.values())))