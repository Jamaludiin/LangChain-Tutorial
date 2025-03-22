
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
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

# Creating a HumanMessage with attributes
human_message = HumanMessage(
    content="What is your name?",
    additional_kwargs={"context": "casual conversation"},
    id="msg_12345",
    name="User",
    response_metadata={"source": "chatbot"},
)

# Creating a SystemMessage to define AI behavior
system_message = SystemMessage(content="You are a helpful assistant! Your name is Bob.")

# Print message attributes
print("Human Message Content:", human_message.content)  # Getting text content
print("Human Message ID:", human_message.id)
print("Human Message Name:", human_message.name)
print("Additional Data:", human_message.additional_kwargs)
print("Response Metadata:", human_message.response_metadata)
print("Pretty Representation:", human_message.pretty_repr())

# Sending messages to Groq API and getting a response
messages = [system_message, human_message]

response = llm.invoke(messages)

# Print AI response
print("\nAI Response:", response)
