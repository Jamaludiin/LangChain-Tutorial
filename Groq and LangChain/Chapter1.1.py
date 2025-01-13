from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the ChatGroq model
chat = ChatGroq(
    #groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# Create a simple message
messages = [
    HumanMessage(content="What is the capital of France?")
]

# Get the response
response = chat.invoke(messages)

# Print the response
print(response.content)
