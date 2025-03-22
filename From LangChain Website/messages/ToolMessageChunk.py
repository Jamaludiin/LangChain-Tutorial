"""
📌 What is ToolMessageChunk?
ToolMessageChunk is a message class used to represent a chunk of a response from a tool execution. It contains:

    Content: The actual message content.
    Tool Call ID: The ID of the tool call it is responding to.
    Status: Whether the tool execution was successful or not.
    Metadata, Artifacts, and IDs: Additional optional information.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages.tool import ToolMessageChunk

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

# Example: Simulating a tool response using ToolMessageChunk
tool_message = ToolMessageChunk(
    content="The sum of 5 + 5 is 10.",  # Actual message content
    tool_call_id="math_123",  # Unique tool call ID
    status="success",  # Status of the tool invocation
    id="msg_001",  # Optional unique ID
    name="MathTool",  # Optional human-readable name
    response_metadata={"model": "math_tool_v1"},  # Optional metadata
)

# Display the properties using the built-in attributes
print("🔹 Text Content:", tool_message.content)  # ✅ Use .content instead of .text()
print("🔹 Pretty Print:")
tool_message.pretty_print()  # ✅ Pretty print
print("🔹 Pretty Representation:", tool_message.pretty_repr(html=False))  # ✅ Formatted text representation
