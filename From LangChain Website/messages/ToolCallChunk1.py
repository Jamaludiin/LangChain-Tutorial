
import os
import json
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import AIMessageChunk
from langchain_core.messages.tool import ToolCallChunk
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

# Define a multiplication tool
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

# Bind the tool to the model
model_with_tools = llm.bind_tools([multiply])

# Simulating partial tool call responses
left_chunk = ToolCallChunk(name="multiply", args='{"a":', index=0)
right_chunk = ToolCallChunk(name=None, args='5, "b": 6}', index=0)

# Merge chunks
merged_tool_call = (
    AIMessageChunk(content="", tool_call_chunks=[left_chunk]) +
    AIMessageChunk(content="", tool_call_chunks=[right_chunk])
).tool_call_chunks[0]

# **Fix:** Ensure merged_tool_call is a ToolCallChunk, not a dict
if isinstance(merged_tool_call, dict):
    tool_name = merged_tool_call.get("name")
    tool_args = merged_tool_call.get("args")
else:
    tool_name = merged_tool_call.name
    tool_args = merged_tool_call.args

# Convert args string to dictionary
parsed_args = json.loads(tool_args)

# **Updated Fix: Use `invoke` instead of `__call__`**
if tool_name == "multiply":
    result = multiply.invoke(parsed_args)  # ✅ Correct way to call the tool
    print(f"✅ Final Result: {result}")  # Output: 30
