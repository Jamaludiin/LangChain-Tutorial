#BaseChatMessageHistory.py
#simple example to demonstrate the BaseChatMessageHistory
# working

from dotenv import load_dotenv
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import AIMessage, HumanMessage

# Load environment variables
load_dotenv()

# Get Groq API key
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Custom in-memory chat history implementation
class InMemoryChatMessageHistory(BaseChatMessageHistory):
    """A simple in-memory implementation of BaseChatMessageHistory."""

    def __init__(self):
        self._messages = []

    @property
    def messages(self):
        return self._messages

    def add_messages(self, messages):
        """Add a list of messages to history."""
        self._messages.extend(messages)

    def clear(self):
        """Clear all messages from history."""
        self._messages = []

# Create an instance of our custom message history
history = InMemoryChatMessageHistory()

# Initialize the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly AI assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Create memory instance using our custom message history
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    chat_memory=history,
)

# Define the LLM chain
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory
)

# Prompt 1: Store user's name
q1 = {"input": "My name is Leon"}
resp1 = chain.invoke(q1)
print(resp1["text"])

# Prompt 2: Ask AI to recall the name
q2 = {"input": "What is my name?"}
resp2 = chain.invoke(q2)
print(resp2["text"])



"""
Explanation:
    InMemoryChatMessageHistory:
    Extends BaseChatMessageHistory.
    Stores messages in a list (self._messages).
    Implements add_messages() to store a batch of messages.
    Implements clear() to reset the conversation history.
    ConversationBufferMemory uses this custom history class.
    The LLMChain remembers previous interactions.

This example demonstrates how to store, retrieve, and use chat history 
without an external database, similar to UpstashRedisChatMessageHistory. Let me know if you need further improvements! 🚀
"""