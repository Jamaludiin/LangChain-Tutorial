import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from typing import TypedDict
from dotenv import load_dotenv

# Define OutputTokenDetails class
class OutputTokenDetails(TypedDict, total=False):
    """Breakdown of output token counts."""
    audio: int
    reasoning: int

# Load environment variables
load_dotenv()

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Example conversation with token tracking
def chat_with_token_details():
    # Create a prompt that encourages chain-of-thought reasoning
    prompt = "Solve this math problem step by step: What is 15% of 80?"
    
    response = llm.invoke(prompt)
    
    # Create an AIMessage with token details
    message = AIMessage(
        content=response.content,
        additional_kwargs={
            "token_details": OutputTokenDetails(
                reasoning=150,  # Example count for reasoning tokens
                audio=0        # No audio tokens in this case
            )
        }
    )
    
    # Print the response and token details
    print("Response:", message.content)
    print("\nToken Details:")
    print(f"Reasoning tokens: {message.additional_kwargs['token_details']['reasoning']}")
    print(f"Audio tokens: {message.additional_kwargs['token_details']['audio']}")

if __name__ == "__main__":
    chat_with_token_details()
