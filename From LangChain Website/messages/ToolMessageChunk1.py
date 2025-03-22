"""
Why Use ToolMessageChunk in LangChain?
The ToolMessageChunk class is useful when working with LLMs that interact with external tools (e.g., calculators, APIs, databases). It helps structure tool responses so they can be used effectively in the conversation.

🔹 Benefits of Using ToolMessageChunk:
✅ Clear Structure → Helps organize tool responses with metadata (e.g., tool name, status, ID).
✅ Better LLM Integration → Ensures models process tool results correctly in multi-turn conversations.
✅ Improved Debugging → Allows tracking tool outputs separately from AI responses.


"""


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.messages.tool import ToolMessageChunk

# Load API key from environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the LLM (Groq API)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# User asks a math question
user_message = HumanMessage(content="What is 7 * 8?")

# Simulate a tool's response using ToolMessageChunk
tool_response = ToolMessageChunk(
    content="The result of 7 * 8 is 56.",  # Tool's answer
    tool_call_id="math_001",  # Unique tool call ID
    status="success",  # Status of the tool invocation
    id="msg_002",  # Optional unique ID
    name="MultiplicationTool",  # Optional tool name
)

# LLM processes the user message and tool response
response = llm.invoke([user_message, tool_response])

# Print outputs
print("🔹 Tool Response:", tool_response.content)  # Structured tool output
print("🔹 LLM Response:", response.content)  # LLM-generated response
