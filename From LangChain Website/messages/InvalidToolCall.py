import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.messages.tool import InvalidToolCall
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq API
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define messages, including an InvalidToolCall (which is a dict-like object)
messages = [
    SystemMessage(content="You are a chatbot that provides weather updates."),
    HumanMessage(content="What’s the weather like in New York?", id="user1", name="John"),
    AIMessage(content="Let me check the weather for you."),
    
    # Simulating an invalid tool call (as a dictionary, not an instance)
    {
        "type": "invalid_tool_call",
        "name": "get_weather",
        "args": None,  # No arguments provided (error)
        "id": "tool1",
        "error": "Missing required location parameter for weather lookup.",
    },
]

# Process messages and handle errors
for msg in messages:
    if isinstance(msg, dict) and msg.get("type") == "invalid_tool_call":
        print(f"\n⚠️ Invalid Tool Call Detected: {msg.get('name')}")
        print(f"🔹 Error Message: {msg.get('error')}\n")
    else:
        print(f"{msg.__class__.__name__}: {msg.content}")

# Invoke Groq model with valid messages (excluding InvalidToolCall)
valid_messages = [msg for msg in messages if not (isinstance(msg, dict) and msg.get("type") == "invalid_tool_call")]
response = llm.invoke(valid_messages)

# Print Groq model response
print("\n--- Groq Model Response ---")
print(response)
