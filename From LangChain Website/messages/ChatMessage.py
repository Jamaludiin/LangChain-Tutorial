# This example shows how to create a conversation between a user and an AI using ChatMessage, then process the response using ChatGroq
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import ChatMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Create a user message using ChatMessage
user_message = ChatMessage(
    content="What is the capital of France?",
    role="user"
)

# Send the message to the AI model
ai_response = llm.invoke([user_message])

# Print the AI's response
print(ai_response.content)


"""
3. Using ChatMessage
When you use ChatMessage, you can explicitly set the role of the message (e.g., user, assistant, system), making it useful for maintaining a structured conversation.

What Happens?
    The response is stored with a role (assistant, user, etc.).
    Useful for multi-turn conversations, where distinguishing between messages is important.

🛠️ When Should You Use Each Approach?
    Approach	                            When to Use
    Direct Output (response.content)	    If you just need to print the AI's response and don't care about structure.
    AIMessage	                            When working with LangChain and need a structured AI response.
    ChatMessage	                            When building chat-like interactions where distinguishing roles (user, assistant, system) is useful.

    
🔹 Key Takeaway
ChatMessage and AIMessage help structure responses for better organization and handling, especially in conversational AI applications.
If you're just retrieving a simple answer, response.content is enough.
If you're building a multi-turn chatbot or storing structured conversations, ChatMessage is more useful.

"""