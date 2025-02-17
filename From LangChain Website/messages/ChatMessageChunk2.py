
# working
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import ChatMessageChunk, AIMessage, HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500,
    timeout=10,
    max_retries=2,
)

# Create a user message (input from the user)
user_message = HumanMessage(content="What is the importance of AI in education?")

# Send the message to the LLM and get a response
response = llm.invoke([user_message])

# Simulate receiving a message chunk from AI
message_chunk = ChatMessageChunk(
    content=response.content,
    role="ai"
)

# Print the message chunk details
print("Message Chunk Content:", message_chunk.content)
print("Message Role:", message_chunk.role)

# Use AIMessage to represent a full AI response
ai_message = AIMessage(
    content=response.content,
    additional_kwargs={"source": "Groq AI"}
)

# Print AI message details
print("AI Message Content:", ai_message.content)
print("Additional Info:", ai_message.additional_kwargs)
