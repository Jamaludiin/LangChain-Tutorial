from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_message_histories.upstash_redis import UpstashRedisChatMessageHistory
from langchain.schema import AIMessage, HumanMessage

from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')
upstash_redis_url = os.getenv('UPSTASH_REDIS_URL')
upstash_redis_token = os.getenv('UPSTASH_REDIS_TOKEN')

# Initialize Upstash Redis chat history storage
chat_history = UpstashRedisChatMessageHistory(
    url=upstash_redis_url, 
    token=upstash_redis_token,
    session_id="user123"  # Unique session ID for storing chat history
)

# Initialize the Groq LLM (Llama-3.3-70b-versatile model)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,   # Controls randomness; lower means more predictable responses
    max_tokens=500,     # Maximum response length
    timeout=10,         # Timeout for API calls
    max_retries=2       # Number of retries in case of failure
)

# Add some messages to history (simulating past conversation)
chat_history.add_user_message("Hello, what is LangChain?")
chat_history.add_ai_message("LangChain is a framework that helps developers build applications using LLMs like OpenAI and Groq.")

# Display the stored messages from Redis
print("\nStored Messages in History:")
for msg in chat_history.messages:
    print(f"{msg.type.capitalize()}: {msg.content}")

# Create a chat prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")  # This will be replaced with user input
])

# Initialize memory with Redis chat history (so LLM remembers past chats)
memory = ConversationBufferMemory(
    memory_key="chat_history",  # Key to store conversation history
    return_messages=True,       # Return full message history
    chat_memory=chat_history    # Use Upstash Redis chat history
)

# Create an LLM chain that connects the model with memory and prompt
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

# Example: Sending a new message to the chat model
user_input = {"input": "Can you explain LangChain's memory system?"}
response = chain.invoke(user_input)

# Display AI's response
print("\nAI Response:")
print(response["text"])

# Store AI's response in history
chat_history.add_ai_message(response["text"])

# Display updated chat history
print("\nUpdated Chat History:")
for msg in chat_history.messages:
    print(f"{msg.type.capitalize()}: {msg.content}")

# Clear chat history (optional)
# chat_history.clear()


"""
How This Works
    Loads the Groq & Upstash Redis credentials from a .env file.
    Creates an Upstash Redis chat history instance (UpstashRedisChatMessageHistory).
    Adds some initial messages to simulate a past conversation.
    Displays stored messages before sending new input.
    Sets up memory (ConversationBufferMemory) to make the LLM remember previous messages.
    Uses LLMChain to process user input with the prompt and memory.
    Stores AI’s new response into Redis and prints the updated conversation.

"""