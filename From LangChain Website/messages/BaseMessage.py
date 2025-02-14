# a simple, straightforward example of using BaseMessage with Groq. However, note that we typically use the specific message types (like HumanMessage or AIMessage) rather than BaseMessage directly.
# error 
"""
Why This Fix Works
BaseMessage is abstract, meaning it cannot be used directly.
HumanMessage represents user input, and AIMessage represents AI-generated responses.
The error "Got unknown type" happens because BaseMessage is not recognized by _convert_message_to_dict.
Try this updated code, and it should work without issues! 🚀
"""

import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Create a user message
user_message = BaseMessage(
    content="What is the capital of France?",  # User's question
    type="human",  # Message type
    id="12345"  # Optional message ID
)

# Send the message and get AI response
response = llm.invoke([user_message])

# Print AI response
print(response)
