import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessageChunk, filter_messages
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq API
groq_api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define a list of messages including a SystemMessageChunk
messages = [
    SystemMessageChunk(content="You are a helpful chatbot.", id="sys1", name="System Init"),
    HumanMessage(content="Hello, can you help me?", id="user1", name="John"),
    AIMessage(content="Of course! What do you need help with?", id="ai1", name="ChatBot"),
    HumanMessage(content="What is the capital of France?", id="user2", name="John"),
    AIMessage(content="The capital of France is Paris.", id="ai2", name="ChatBot"),
]

# Print the original messages
print("\n--- All Messages ---")
for msg in messages:
    print(f"{msg.name}: {msg.content}")

# Filter messages: Only include HumanMessage and AIMessage
filtered_messages = filter_messages(messages, include_types=[HumanMessage, AIMessage])

# Pass filtered messages to Groq model
response = llm.invoke(filtered_messages)

# Print the filtered messages
print("\n--- Filtered Messages Sent to Groq Model ---")
for msg in filtered_messages:
    print(f"{msg.name}: {msg.content}")

# Print the response from the Groq model
print("\n--- Groq Model Response ---")
print(response)
