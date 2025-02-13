from typing import TypedDict
import os
from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

class OutputTokenDetails(TypedDict, total=False):
    """Breakdown of output token counts."""
    audio: int
    reasoning: int

def chat_with_token_tracking():
    # Load environment variables
    load_dotenv()
    
    # Initialize the Groq chat model
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
    )
    
    # Create a prompt
    prompt = "Solve this math problem step by step: What is 15% of 80?"
    
    # Get response
    response = llm.invoke(prompt)
    
    # Create token details directly
    token_details = OutputTokenDetails(
        reasoning=150,  # Example count for reasoning tokens
        audio=0        # No audio tokens in this case
    )
    
    # Print the response and token details
    print("Response:", response.content)
    print("\nToken Details:")
    print(f"Reasoning tokens: {token_details['reasoning']}")
    print(f"Audio tokens: {token_details['audio']}")

if __name__ == "__main__":
    chat_with_token_tracking()