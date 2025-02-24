import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessageChunk
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

# Create a system message chunk
system_message = SystemMessageChunk(
    content="This is a system message for initializing conversation rules.",
    id="sys-001",
    name="Initialization Message",
    additional_kwargs={"source": "admin"},
    response_metadata={"token_count": 10}
)

# Print message properties
print("Message Content:", system_message.content)  # Use .content instead of .text()
print("Message ID:", system_message.id)  # Get the message ID
print("Message Name:", system_message.name)  # Get the optional name
print("Additional Data:", system_message.additional_kwargs)  # Get extra metadata
print("Response Metadata:", system_message.response_metadata)  # Get response metadata
print("Pretty Representation:", system_message.pretty_repr())  # Get formatted output
