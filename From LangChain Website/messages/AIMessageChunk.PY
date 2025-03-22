# This script demonstrates how to get an AI-generated response, chunk the message, and explore its attributes. 🚀
# working

import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessageChunk
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

# Define a user prompt
user_prompt = "Explain the importance of AI in modern business."

# Get the AI response
response = llm.invoke(user_prompt)

# Simulating chunked response (Splitting content into chunks)
chunks = response.content.split(". ")  # Split by sentences for simplicity

# Creating an AIMessageChunk object
ai_message_chunk = AIMessageChunk(
    content=chunks[0],  # Taking the first sentence as a chunk
    response_metadata={"token_usage": 20, "model": "llama-3.3-70b"},
    id="chunk_001",
    name="AI Chunk Message"
)

# 🖨 Printing the outputs with clear formatting
print("\n🔹 AIMessageChunk Example:")
print("🟢 Content:", ai_message_chunk.content)
print("🟢 ID:", ai_message_chunk.id)
print("🟢 Name:", ai_message_chunk.name)
print("🟢 Response Metadata:", ai_message_chunk.response_metadata)

# Using pretty_print() for formatted output
print("\n🔹 Pretty Print:")
ai_message_chunk.pretty_print()

# Using pretty_repr() for HTML output
print("\n🔹 Pretty Representation (HTML Format):")
print(ai_message_chunk.pretty_repr(html=True))




"""
📝 What This Example Covers
✅ Uses ChatGroq to generate a response
✅ Creates an AIMessageChunk instance
✅ Demonstrates attributes like content, response_metadata, and pretty_print()
✅ Formatted output for clarity
"""