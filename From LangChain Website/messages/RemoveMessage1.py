import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.messages.modifier import RemoveMessage

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

# Sample conversation messages
messages = [
    SystemMessage(content="You are an AI assistant."),
    HumanMessage(content="Hello, how are you?", id="msg-100"),
    AIMessage(content="I'm doing great! How can I assist you today?", id="msg-101"),
    HumanMessage(content="Tell me a joke.", id="msg-102"),
    AIMessage(content="Why don’t skeletons fight each other? Because they don’t have the guts!", id="msg-103"),
    HumanMessage(content="That's funny! Now tell me about Python programming.", id="msg-104"),
    AIMessage(content="Python is a powerful, easy-to-learn programming language used in web development, AI, and more.", id="msg-105"),
    
    # Messages to be removed
    RemoveMessage(id="msg-101"),  # Remove AI's first response
    RemoveMessage(id="msg-103"),  # Remove AI's joke response
    RemoveMessage(id="msg-105")   # Remove AI's Python explanation
]

# ✅ Remove messages that are marked for deletion
delete_ids = {msg.id for msg in messages if isinstance(msg, RemoveMessage)}
filtered_messages = [msg for msg in messages if msg.id not in delete_ids]

# Generate response using Groq API
response = llm.invoke(filtered_messages)

# Print the AI response
print(response.content)
