import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from dotenv import load_dotenv
from typing import TypedDict

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Simulate an AI response with token breakdown
ai_response = AIMessage(
    content="This is an AI-generated response with reasoning and audio tokens.",
    additional_kwargs={
        "token_usage": {
            "completion_tokens": 200,
            "prompt_tokens": 10,
            "total_tokens": 210
        }
    }
)

# Print output token details
print("AI Response:", ai_response.content)
print("Output Token Details:", ai_response.additional_kwargs["token_usage"])

class OutputTokenDetails(TypedDict, total=False):
    """Breakdown of output token counts."""
    audio: int
    reasoning: int
