# BaseChatLoader.py
import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain_core.chat_loaders import BaseChatLoader
from langchain_core.chat_sessions import ChatSession
from langchain_groq import ChatGroq

class CustomChatLoader(BaseChatLoader):
    def __init__(self, session_data):
        self.session_data = session_data  # List of chat history

    def lazy_load(self):
        """Lazy load chat sessions one by one"""
        for session in self.session_data:
            yield ChatSession(messages=session)

    def load(self):
        """Eagerly load all chat sessions into memory"""
        return [ChatSession(messages=session) for session in self.session_data]

# Example chat history (mock data)
chat_history = [
    [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there!"}],
    [{"role": "user", "content": "Tell me a joke"}, {"role": "assistant", "content": "Why did the AI cross the road? To optimize the route!"}],
]

# Create chat loader
loader = CustomChatLoader(chat_history)

# Lazy load chat sessions
for session in loader.lazy_load():
    print(session)

# Eagerly load chat sessions
all_sessions = loader.load()
print(all_sessions)




groq_api_key = os.getenv('GROQ_API_KEY')

groq_chat = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=32767,
        timeout=10,
        max_retries=2,
    )

# Using Groq for chat completion
response = groq_chat.invoke("What is Upstash Redis?")
print("\n",response.content, "\n")



"""
Steps Covered:
Create a Custom Chat Loader by inheriting BaseChatLoader.
Load Chat Sessions (either eagerly or lazily).
Use Groq API for chat completions.
"""


"""
What This Code Does:
Defines a custom chat loader (CustomChatLoader) that extends BaseChatLoader.
Implements lazy_load() to yield chat sessions one by one (efficient for large data).
Implements load() to load all sessions into memory at once.
Mocks chat history for demonstration purposes.
Uses Groq API (ChatGroq) to generate chat completions.
"""