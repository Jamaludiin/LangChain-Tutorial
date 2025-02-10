# working and he remeber the conversation

import os
from langchain_core.chat_sessions import ChatSession
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Get API key for Groq
groq_api_key = os.getenv('GROQ_API_KEY')
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

# Initialize Groq LLM client
groq_llm = ChatGroq(
    model="llama-3.3-70b-versatile",  # Use your Groq model of choice
    temperature=0.7,
    max_tokens=500,
    timeout=10,
    max_retries=2,
)


class SimpleChat:
    def __init__(self, chat_data=None):
        """
        Initializes the chat session with predefined messages.
        """
        self.session = ChatSession()  # Store full chat history
        if chat_data:
            self.load_messages(chat_data)

    def load_messages(self, chat_data):
        """
        Load predefined messages into the chat session.
        """
        for sender, message in chat_data:
            if sender == "AI":
                self.session.add_message(AIMessage(content=message))
            else:
                self.session.add_message(HumanMessage(content=message))

    def chat(self, user_message):
        """
        Continue the conversation while maintaining full context.
        """
        # Add the user's message to session history
        self.session.add_message(HumanMessage(content=user_message))

        # Convert all chat history into a single conversation string
        history_text = "\n".join([f"{msg.content}" for msg in self.session.messages])

        # Generate response using the full history as context
        response = groq_llm.invoke(history_text)

        # Add AI response to session
        ai_message = AIMessage(content=response.content)
        self.session.add_message(ai_message)

        return ai_message.content  # Return response text

    def get_chat_history(self):
        """
        Retrieve the full chat history.
        """
        return [(msg.__class__.__name__, msg.content) for msg in self.session.messages]


# Example predefined chat data (optional)
chat_data = [
    ("Human", "Hello! How are you?"),
    ("AI", "I'm doing great, thank you! How about you?"),
    ("Human", "I'm good, thanks for asking!"),
    ("AI", "You're welcome!"),
]

# Initialize chat session with predefined messages
chat = SimpleChat(chat_data)

# Interactive chat loop
print("Chat with Groq AI! (Type 'exit' to end chat)\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    # Get AI response
    response = chat.chat(user_input)
    print("\nAI:", response)

    # Optionally print chat history for debugging
    print("\nChat History:")
    for sender, msg in chat.get_chat_history():
        print(f"{sender}: {msg}")




"""
Explanation:
    Groq Setup:
        The ChatGroq model is initialized with a specific model, temperature, max tokens, and other parameters.
    ChatSession Class:
        SimpleChat class manages chat history using ChatSession.
        load_messages loads predefined messages into the session if provided.
        The chat method adds user input to the session and uses the accumulated conversation history to generate a response.
    Memory:
        The conversation history is stored within the session, and Groq’s model leverages it for better context-aware responses.
    Interactive Loop:
        The chat allows for continuous user input, generates a response, and displays both the conversation history and the response.

How It Works:
User Input: 
    Each user input is appended to the session.
Groq API Call: 
    The complete conversation history is passed to Groq to generate context-aware responses.
Memory: 
    AI remembers everything said in the conversation, enabling more natural and context-rich exchanges.
Additional Features:
    You can customize the predefined messages (chat_data) as per your requirements.
    It supports an interactive chat session where the user can type exit or quit to stop the conversation.


"""