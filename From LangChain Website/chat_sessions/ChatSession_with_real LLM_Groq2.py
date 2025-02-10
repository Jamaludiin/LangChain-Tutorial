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
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)


class SimpleChat:
    def __init__(self, chat_data):
        """
        Initializes the chat session with predefined messages.
        """
        self.session = ChatSession()  # Store full chat history
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


# Example predefined chat data
chat_data = [
    ("Human", "Hello! How are you?"),
    ("AI", "I'm doing great, thank you! How about you?"),
    ("Human", "I'm good, thanks for asking!"),
    ("AI", "You're welcome!"),
]

# Initialize chat session with predefined messages
chat = SimpleChat(chat_data)

# Interactive chat
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    response = chat.chat(user_input)
    print("\nAI:", response)

    # Print chat history for debugging
    print("\nChat History:")
    for sender, msg in chat.get_chat_history():
        print(f"{sender}: {msg}")
