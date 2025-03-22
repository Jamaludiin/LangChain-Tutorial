import os
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
    max_tokens=100,
    timeout=10,
    max_retries=2,
)

# Define a multiplication tool
@tool
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

# Simulating partial tool call chunks
left_chunk = ToolCallChunk(name="multiply", args='{"a":', index=0)
right_chunk = ToolCallChunk(name=None, args='5, "b": 6}', index=0)

# Merging tool call chunks
merged_chunks = (
    AIMessageChunk(content="", tool_call_chunks=[left_chunk])
    + AIMessageChunk(content="", tool_call_chunks=[right_chunk])
).tool_call_chunks

# Display merged result
print("Merged Tool Call Chunks:", merged_chunks)


"""
The point of ToolCallChunk is to handle streaming tool calls efficiently when using LLMs that output responses in parts rather than all at once.

Why is ToolCallChunk Needed?
    LLMs Output Text in Chunks (Streaming)
        When an LLM is generating a response, it might not return the entire tool call in one go.
        Instead, the LLM streams partial outputs (e.g., "a": in one chunk and 5, "b":6} in another).
    
    Merging Partial Chunks into a Complete Tool Call
        ToolCallChunk helps combine these parts into a full, valid function call.
        Without it, the system might fail to recognize an incomplete tool call.
    
    Efficient and Continuous Processing
        Instead of waiting for the entire response before processing, ToolCallChunk lets you handle tool calls as they arrive.
        This makes LLM-driven applications faster and more responsive.

"""