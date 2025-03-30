from langchain_core.messages import messages_from_dict

# Define messages as a list of dictionaries
messages_dict = [
    {"type": "human", "content": "Hello!"},
    {"type": "ai", "content": "Hi there! How can I assist you?"},
    {"type": "human", "content": "What is LangChain?"}
]

# Convert to BaseMessage objects
messages = messages_from_dict(messages_dict)

# Print the converted messages
for msg in messages:
    print(f"{msg.type}: {msg.content}")


"""
What messages_from_dict Does
The messages_from_dict method in LangChain converts a sequence of message dictionaries (JSON-like structures) into BaseMessage objects. These objects allow for structured handling of messages in conversational AI applications.


Example of Why It's Useful
If you're integrating a chatbot with a frontend that sends messages as JSON, messages_from_dict helps you convert those messages into a format your backend can process efficiently.


In LangChain, BaseMessage is an abstract class that serves as the foundation for different types of messages, such as system, AI, and human messages. Here’s how it looks internally:

BaseMessage Structure

from langchain_core.messages import BaseMessage

class BaseMessage:
    content: str  # The message text
    role: str  # Role of the sender (e.g., "user", "system", "assistant")

    def __init__(self, content: str, role: str):
        self.content = content
        self.role = role

        

Types of Messages in LangChain
LangChain has different message classes that inherit from BaseMessage:

SystemMessage – Instructions for the AI

AIMessage – Responses from the AI

HumanMessage – User input


"""