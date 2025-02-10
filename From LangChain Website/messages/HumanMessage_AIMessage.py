# not working
# he can remmeber past conversation
import os
from langchain_core.chat_sessions import ChatSession
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key for Groq
groq_api_key = os.getenv('GROQ_API_KEY')
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

# Initialize Groq Chat model
groq_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500,
    timeout=10,
    max_retries=2,
)

# Create a list to store message history
messages = []

# Start interactive chat loop
print("Chat with Groq AI! (Type 'exit' to end chat)\n")
while True:
    # Get user input
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Exiting chat. Goodbye!")
        break

    # Add user message to history
    messages.append(HumanMessage(content=user_input))

    # Send complete message history to LLM
    response = groq_llm.invoke(messages)

    # Add AI response to history
    messages.append(AIMessage(content=response.content))

    # Display response
    print(f"AI: {response.content}\n")

# Display full chat history at the end
print("\n=== Chat History ===")
for msg in messages:
    sender = "You" if isinstance(msg, HumanMessage) else "AI"
    print(f"{sender}: {msg.content}")




"""
The confusion arises because there's been a change in LangChain's architecture. The ChatSession class from langchain_core.chat_sessions is primarily meant to be an internal implementation detail and doesn't provide the functionality we might expect from its name.
Here's why we can't use it as intended:
The ChatSession class in LangChain is more of a data structure for internal use rather than a full-featured chat session manager.
It doesn't provide built-in methods for managing message history in the way we want.
The error we saw (AttributeError: 'dict' object has no attribute 'messages') occurs because the class doesn't expose a messages attribute as we might expect.
If you want to create a more structured chat session manager, you could create your own class like this:
"""
"""
How It Works:
✅ Uses LangChain's ChatSession to store chat history.
✅ Uses Groq's LLM (ChatGroq) to generate responses.
✅ Supports interactive chat in a loop.
✅ Ends when user types "exit".
✅ Displays full chat history at the end."""