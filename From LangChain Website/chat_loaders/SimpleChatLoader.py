# working 

import os
from langchain_core.chat_sessions import ChatSession
from langchain_core.messages import HumanMessage, AIMessage
from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key for Groq
groq_api_key = os.getenv('GROQ_API_KEY')
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

# Initialize Groq LLM client
groq_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)


class SimpleChatLoader:
    def __init__(self, chat_data):
        """
        Initializes the chat loader with provided chat data.
        """
        self.messages = []  # Use a direct list instead of ChatSession
        self.load_messages(chat_data)  # Load predefined messages

    def load_messages(self, chat_data):
        """
        Load predefined messages into the messages list.
        """
        for sender, message in chat_data:
            if sender == "AI":
                self.messages.append(AIMessage(content=message))
            else:
                self.messages.append(HumanMessage(content=message))

    def chat(self, user_message):
        """
        Continue the conversation with the Groq LLM.
        """
        # Add user message to session
        self.messages.append(HumanMessage(content=user_message))

        # Generate response from LLM
        response = groq_llm.invoke(user_message)

        # Add AI response to session
        ai_message = AIMessage(content=response.content)
        self.messages.append(ai_message)

        return ai_message.content  # Return response text

    def get_chat_history(self):
        """
        Retrieve the chat history.
        """
        return [(msg.__class__.__name__, msg.content) for msg in self.messages]


# Example predefined chat data
chat_data = [
    ("Human", "Hello! How are you?"),
    ("AI", "I'm doing great, thank you! How about you?"),
    ("Human", "I'm good, thanks for asking!"),
    ("AI", "You're welcome!"),
]

# Initialize chat session with predefined messages
chat_loader = SimpleChatLoader(chat_data)

# Interactive chat
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    response = chat_loader.chat(user_input)
    print("\nAI:", response)

    # Print chat history for debugging
    print("\nChat History:")
    for sender, msg in chat_loader.get_chat_history():
        print(f"{sender}: {msg}")
