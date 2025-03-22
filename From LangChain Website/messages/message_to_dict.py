
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, message_to_dict
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

# Create a HumanMessage
human_msg = HumanMessage(content="Hello, how are you?")


# Convert HumanMessage to dictionary
human_msg_dict = message_to_dict(human_msg)


# Print the dictionary format of the message
print(human_msg_dict)



# Example output:
# {'type': 'human', 'data': {'content': 'Hello, how are you?'}}
