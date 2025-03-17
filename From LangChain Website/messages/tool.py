import os
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

# Print result
print(response)
print("\n content")
print(response.content)
print("Tool Calls:", response.tool_calls)
tool_result = response.tool_calls

results = {}
print("Tool results:")

for tool_call in tool_result:
    tool_name = tool_call["name"]
    args = tool_call["args"]

    if tool_name == "multiply":
        results[tool_call["id"]] = multiply.invoke(args)  # Fix: use .invoke()
        print("\nmultiply Results:", results, "\n")


"""
Your code is correctly binding the multiply tool to model_with_tools, but the issue is that the model only returns a tool call request instead of executing it automatically.

🔍 Issue: The Model Is Only Calling the Tool, Not Executing It
Your output shows this:


"tool_calls": [
    {
        "name": "multiply",
        "args": {"a": 5, "b": 6},
        "id": "call_ensm",
        "type": "tool_call"
    }
]
This means:

The model recognized that a tool should be used.
It did NOT execute the tool (it only returned a request to call it).
You need to manually execute the tool after the model suggests it.

"""