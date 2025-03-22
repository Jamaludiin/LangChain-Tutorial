import os
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.messages.utils import filter_messages
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Groq API key from the environment
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Creating a list of messages
messages = [
    SystemMessage("Hello! I'm your AI assistant."),
    HumanMessage("What is the capital of France?", id="msg_1", name="user_1"),
    AIMessage("The capital of France is Paris.", id="msg_2", name="ai_1"),
    HumanMessage("Tell me a joke.", id="msg_3", name="user_2"),
    AIMessage("Why don't scientists trust atoms? Because they make up everything!", id="msg_4", name="ai_2"),
]


# Filtering messages to include only HumanMessages and exclude AI responses
filtered_msgs = filter_messages(
    messages,
    include_types=("human",),  # Only include messages from human users
    exclude_ids=("msg_3",),    # Exclude a specific message
)

# Display the filtered messages
for msg in filtered_msgs:
    print(f"{msg.type}: {msg.content}")



"""
🚀 Why Use filter_messages?
It helps filter conversations dynamically.
Useful for preprocessing messages before sending them to an AI model.
Reduces noise by filtering unnecessary messages.
"""