# working
# This version properly generates an HTML output using Python's built-in html module.
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

# Using real HTML formatting
html_output = f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Message Chunk</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .container {{ border: 2px solid #333; padding: 15px; border-radius: 8px; background-color: #f9f9f9; }}
        h2 {{ color: #007bff; }}
        p {{ font-size: 16px; }}
    </style>
</head>
<body>
    <div class="container">
        <h2>AIMessageChunk Message</h2>
        <p><strong>Name:</strong> {ai_message_chunk.name}</p>
        <p><strong>Content:</strong> {ai_message_chunk.content}</p>
        <p><strong>ID:</strong> {ai_message_chunk.id}</p>
        <p><strong>Response Metadata:</strong> {ai_message_chunk.response_metadata}</p>
    </div>
</body>
</html>
"""

# Printing HTML output
print("\n🔹 Proper HTML Formatted Output:")
print(html_output)
