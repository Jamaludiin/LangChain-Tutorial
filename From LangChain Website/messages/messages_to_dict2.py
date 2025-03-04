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

# Create a sequence of messages (conversation)
messages = [
    HumanMessage(content="Hello, how are you?"),
    AIMessage(content="I'm an AI model! How can I assist you today?")
]

# Convert messages to list of dictionaries
messages_dict_list = messages_to_dict(messages)

# Print the dictionary format of the messages
print(messages_dict_list)

# Example output:
# [
#     {'type': 'human', 'data': {'content': 'Hello, how are you?'}},
#     {'type': 'ai', 'data': {'content': "I'm an AI model! How can I assist you today?"}}
# ]
