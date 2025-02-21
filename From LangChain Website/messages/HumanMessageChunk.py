

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessageChunk

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=100,
    timeout=10,
    max_retries=2,
)

# Create a chunked human message
human_message_chunk = HumanMessageChunk(
    content="Hello, how are you?",
    id="msg-123",  # Unique identifier for the message
    name="UserMessage",  # Optional readable name
    example=False,  # Not part of an example conversation
    response_metadata={"token_count": 5}  # Metadata example
)

# Display message properties
print("Message Content:", human_message_chunk.content)  # Access message text
print("Message ID:", human_message_chunk.id)
print("Message Name:", human_message_chunk.name)
print("Response Metadata:", human_message_chunk.response_metadata)
print("Pretty Representation:", human_message_chunk.pretty_repr())  # Pretty format

# Send the message to the LLM
response = llm.invoke([human_message_chunk])
print("\nAI Response:", response.content)
