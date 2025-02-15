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

# Concatenating message chunks
full_message = chunk1.content + " " + chunk2.content

# Send concatenated message to Groq model
response = llm.invoke(full_message)

# Print the AI's response
print("Full Message:", full_message)
print("AI Response:", response)


"""
When Should You Use BaseMessageChunk?
    If you're working with multiple AI-generated messages that need to be processed individually.
    When storing structured responses with metadata.
    If implementing streaming responses where chunks arrive sequentially.

Since Groq doesn’t require chunked messages, it's simpler and more efficient to just send the full message as a string instead. 🚀

"""

"""
The purpose of using BaseMessageChunk is to structure messages into smaller, manageable pieces that can be concatenated or processed separately before being sent to an LLM (like Groq). However, in your case, it might not be necessary because you are manually concatenating the messages before sending them.

Why Use BaseMessageChunk?
    ✅ Structured Message Handling – Helps in storing, tracking, and managing messages in a structured way.
    ✅ Incremental Processing – If working with streaming data, you can process chunks separately before forming a complete response.
    ✅ Metadata Handling – Allows attaching metadata (id, name, response_metadata, etc.) to each chunk for better tracking.
    ✅ Concatenation Support – It allows you to combine multiple message parts logically before passing them to an LLM.

Why This Case Might Not Need It
    Since you're manually concatenating the messages before sending them, you’re not utilizing the benefits of BaseMessageChunk. Instead, you could directly pass the message string to Groq without using BaseMessageChunk at all.
"""