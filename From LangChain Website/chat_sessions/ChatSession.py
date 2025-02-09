# ChatSession.py
# working

import os
from langchain_core.chat_sessions import ChatSession
from langchain_core.messages import HumanMessage, AIMessage

# Simple class to create a chat session from manually provided messages
class SimpleChatLoader:
    def __init__(self, chat_data):
        """
        Initializes the chat loader with provided chat data.
        """
        self.chat_data = chat_data  # chat_data should be a list of (sender, message) tuples

    def load(self):
        """
        Load the chat session eagerly into memory.
        """
        messages = []
        for sender, message in self.chat_data:
            if sender == "AI":
                messages.append(AIMessage(content=message))
            else:
                messages.append(HumanMessage(content=message))
        # Return a ChatSession dictionary
        return {"messages": messages}  # Return as dictionary, not an object

# Example chat data as (sender, message) tuples
chat_data = [
    ("Human", "Hello! How are you?"),
    ("AI", "I'm doing great, thank you! How about you?"),
    ("Human", "I'm good, thanks for asking!"),
    ("AI", "You're welcome!"),
]

# Initialize the loader with the chat data
loader = SimpleChatLoader(chat_data)

# Load the chat session (as dictionary)
chat_session = loader.load()

# Access the messages directly from the dictionary
for msg in chat_session["messages"]:
    print(f"Sender: {msg.__class__.__name__} - Message: {msg.content}")
