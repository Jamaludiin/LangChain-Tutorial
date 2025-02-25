import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from langchain_core.messages.tool import ToolCall  # Import ToolCall
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

# Create a tool call request to "calculate_sum"
tool_request = ToolCall(
    name="calculate_sum",  # The tool we want to call
    args={"a": 5, "b": 10},  # Arguments to pass to the tool
    id="sum_001"  # Unique identifier for tracking
)

# Simulate an AI response using AIMessage
ai_response = AIMessage(
    content="Calculating the sum...",
    tool_calls=[tool_request]
)

# Print the AI's tool request
print("AI Requesting Tool Call:", ai_response)
print("\nThis is the content\n")
print("AI Requesting Tool Call:", ai_response.content)
print("\nThis is the Tool Calls\n")
print("AI Requesting Tool Call:", ai_response.tool_calls)


print("\nThis is the AI or the LLM Calls\n")

# Actually send a message to the AI
response = llm.invoke("What is 5 + 10?")

print("AI Response:", response.content)



"""
 this simulates an AI response but does not actually communicate with an AI or LLM.

Why?
    The script initializes ChatGroq, which is used for communicating with the Groq API (AI model).
    However, no actual request is sent to the LLM (llm.invoke() or llm.predict()).
    The ToolCall and AIMessage objects are manually created to simulate what an AI might do.
Does This Communicate with the AI?
    🚫 No – The script only creates objects (ToolCall, AIMessage) and prints them.
    ✅ Yes (if modified) – If you later use llm.invoke() or similar, it would send a request to the AI.
"""