import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import FunctionMessageChunk
from langchain_core.outputs import ChatGenerationChunk
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

def stream_groq_response(prompt: str):
    """Calls the Groq API and streams responses in chunks using FunctionMessageChunk."""
    response = llm.invoke(prompt, stream=True)  # Enable streaming mode

    for chunk in response:
        if isinstance(chunk, ChatGenerationChunk) and chunk.message.content:
            content = chunk.message.content
            yield FunctionMessageChunk(content=content)

# Example usage
prompt_text = "Explain the benefits of AI in software development."
for chunk in stream_groq_response(prompt_text):
    print(chunk.content, end="", flush=True)  # Simulates real-time streaming
