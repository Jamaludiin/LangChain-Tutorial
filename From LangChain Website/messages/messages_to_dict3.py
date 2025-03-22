import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, messages_to_dict
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

# Create multiple HumanMessage instances
human_msg1 = HumanMessage(content="Hello, how are you?")
human_msg2 = HumanMessage(content="Hello, how are you again?")

# Convert messages to a list of dictionaries
human_msgs_dict = messages_to_dict([human_msg1, human_msg2])

# Print the dictionary format of the messages
print("\nConverted Messages to Dict Format:")
print(human_msgs_dict)

# Example output:
# [
#     {'type': 'human', 'data': {'content': 'Hello, how are you?'}},
#     {'type': 'human', 'data': {'content': 'Hello, how are you again?'}}
# ]
