# InMemoryChatMessageHistory.py
# working

from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.schema import AIMessage, HumanMessage

# Load environment variables (to get the Groq API key from .env file)
load_dotenv()

# Retrieve the Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq LLM (Llama-3.3-70b-versatile model)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,   # Controls randomness; lower means more predictable responses
    max_tokens=1000,    # Maximum response length
    timeout=10,         # Time to wait before request times out
    max_retries=2,      # Number of retries in case of failure
)

# Create an instance of InMemoryChatMessageHistory to store chat history
chat_history = InMemoryChatMessageHistory()

# Add some messages to history (simulating a conversation)
chat_history.add_user_message("Hello, who won the last World Cup?")
chat_history.add_ai_message("The last FIFA World Cup was won by Argentina in 2022.")

# Display the stored messages
print("\nStored Messages in History:")
for msg in chat_history.messages:
    print(f"{msg.type.capitalize()}: {msg.content}")

# Create a prompt template for the chat
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")  # This will be replaced with user input
])

# Initialize memory with chat history (so LLM remembers previous messages)
memory = ConversationBufferMemory(
    memory_key="chat_history",  # Key to store conversation history
    return_messages=True,       # Return full message history
    chat_memory=chat_history    # Use our in-memory chat history
)

# Create an LLM chain that connects the model with memory and prompt
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory
)

# Example: Sending a new message to the chat model
user_input = {"input": "Who was the top scorer in the 2022 World Cup?"}
response = chain.invoke(user_input)

# Display AI's response
print("\nAI Response:")
print(response["text"])

# Store AI's response in history
chat_history.add_ai_message(response["text"])

# Display updated message history
print("\nUpdated Chat History:")
for msg in chat_history.messages:
    print(f"{msg.type.capitalize()}: {msg.content}")

# Clear chat history (optional)
# chat_history.clear()



"""

How This Works
    Loads the Groq API key from a .env file.
    Creates an in-memory chat history (InMemoryChatMessageHistory).
    Manually adds some messages (to simulate a past conversation).
    Displays stored messages before sending new input.
    Sets up a conversation memory (ConversationBufferMemory) so the LLM remembers past chats.
    Uses LLMChain to process user input with the prompt and memory.
    Stores AI's new response into history and prints the updated conversation.


"""