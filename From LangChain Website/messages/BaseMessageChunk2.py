# working


import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessageChunk
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

# Create message chunks with required "type" parameter
chunk1 = BaseMessageChunk(
    content="Hello, this is part 1 of the message.", 
    id="chunk_1", 
    name="Greeting",
    type="ai_message"  # Required field
)

chunk2 = BaseMessageChunk(
    content="Here is part 2 with more details.", 
    id="chunk_2", 
    name="Details",
    type="ai_message"  # Required field
)

# Store chunks in a list for tracking
message_chunks = [chunk1, chunk2]

# Send each chunk separately and track responses
responses = {}
for chunk in message_chunks:
    response = llm.invoke(chunk.content)
    responses[chunk.id] = {
        "chunk_name": chunk.name,
        "content": chunk.content,
        "ai_response": response.content,
        "metadata": response.response_metadata,  # Track AI model metadata
    }

# Print tracking information
for chunk_id, details in responses.items():
    print(f"\nTracking ID: {chunk_id}")
    print(f"Chunk Name: {details['chunk_name']}")
    print(f"User Message: {details['content']}")
    print(f"AI Response: {details['ai_response']}")
    print(f"Metadata: {details['metadata']}")


"""
You can track messages using BaseMessageChunk by leveraging the id, name, and response_metadata. However, your current approach does not fully utilize BaseMessageChunk for tracking. Instead, you are just concatenating message content and sending it as a single string.

How to Properly Track Messages?
To track individual chunks, you can:
    Store metadata (id, name, etc.) in a dictionary or log file.
    Send messages sequentially and record responses.
    Include chunk details in the API response.
"""