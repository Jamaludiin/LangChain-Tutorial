
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
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

# Define messages
messages = [
    SystemMessage(
        content="You are a friendly and knowledgeable assistant named Bob. You always respond in a concise and helpful manner."
    ),
    HumanMessage(
        content="What is your name?"
    )
]

# Get AI response
response = llm.invoke(messages)

# Print response
print(response.content)  # Expected output: "My name is Bob. How can I assist you today?"
