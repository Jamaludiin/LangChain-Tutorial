import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import FunctionMessageChunk
from langchain_core.outputs import ChatGenerationChunk
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("❌ ERROR: GROQ_API_KEY is missing. Check your .env file.")

# Initialize model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

def stream_groq_response(prompt: str):
    """Calls the Groq API and streams responses in chunks."""
    print("🚀 Sending request to Groq API...")

    response = llm.stream(prompt)

    if not response:
        print("⚠️ No response received from API.")
        return

    for chunk in response:
        print(f"🧩 Chunk received: {chunk}")  # Debugging line
        if isinstance(chunk, ChatGenerationChunk) and chunk.message.content:
            content = chunk.message.content
            yield FunctionMessageChunk(content=content)

# Test simple non-streaming response
print("🔍 Testing basic API response...")
print(llm.invoke("Hello, are you working?"))

# Streaming Example
prompt_text = "Explain the benefits of AI in software development."
for chunk in stream_groq_response(prompt_text):
    print(chunk.content, end="", flush=True)
