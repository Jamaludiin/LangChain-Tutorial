# working
# 
"""
How to Fix It Without OpenAI
    You have two options:

    ✅ Option 1: Use a Compatible Hugging Face Tokenizer

    i used Option 2 to fix the error in the other file

    ✅ Option 2: Approximate Token Count
        If you don’t want to install Hugging Face, use a simple word counter:
"""

import os
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, trim_messages
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define a chat history
messages = [
    SystemMessage("You're a helpful assistant."),
    HumanMessage("What's the capital of France?"),
    AIMessage("The capital of France is Paris."),
    HumanMessage("Tell me a fun fact about it."),
    AIMessage("Paris is known as the 'City of Light' because it was one of the first cities to use streetlights."),
    HumanMessage("What are some famous landmarks in Paris?"),
]

# Approximate token counter using word count
def count_tokens(messages):
    text = " ".join(msg.content for msg in messages)
    return len(text.split())  # Approximate token count

# Trim the messages to fit within the token limit
trimmed_messages = trim_messages(
    messages,
    strategy="last",
    token_counter=count_tokens,  # Use our word-based token counter
    max_tokens=30,  # Adjust this limit based on your needs
    start_on="human",
    end_on=("human", "tool"),
    include_system=True
)

# Print the trimmed messages
for msg in trimmed_messages:
    print(f"{msg.__class__.__name__}: {msg.content}")
