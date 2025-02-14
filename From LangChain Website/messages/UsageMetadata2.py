# working but static
import os
from groq import Groq
from langchain_groq import ChatGroq
from typing import TypedDict
from typing_extensions import NotRequired
from dotenv import load_dotenv

# Define the necessary classes
class InputTokenDetails(TypedDict, total=False):
    """Breakdown of input token counts."""
    audio: int
    cache_creation: int
    cache_read: int

class OutputTokenDetails(TypedDict, total=False):
    """Breakdown of output token counts."""
    audio: int
    reasoning: int

class UsageMetadata(TypedDict):
    """Usage metadata for a message."""
    input_tokens: int
    output_tokens: int
    total_tokens: int
    input_token_details: NotRequired[InputTokenDetails]
    output_token_details: NotRequired[OutputTokenDetails]

def chat_with_usage_tracking():
    # Initialize the Groq chat model
    load_dotenv()
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
    )
    
    # Create a prompt that might involve reasoning
    prompt = """Please solve this problem step by step:
    1. Calculate 15% of 80
    2. Then add 25 to the result"""
    
    # Get response
    response = llm.invoke(prompt)
    
    # Create usage metadata
    usage = UsageMetadata(
        input_tokens=50,  # Example count
        output_tokens=150,  # Example count
        total_tokens=200,  # Sum of input and output tokens
        input_token_details={
            "audio": 0,
            "cache_creation": 30,
            "cache_read": 20
        },
        output_token_details={
            "audio": 0,
            "reasoning": 120  # Tokens used in step-by-step reasoning
        }
    )
    
    # Print the conversation with detailed usage statistics
    print("Prompt:", prompt)
    print("\nResponse:", response.content)
    print("\nUsage Statistics:")
    print(f"Input Tokens: {usage['input_tokens']}")
    print(f"Output Tokens: {usage['output_tokens']}")
    print(f"Total Tokens: {usage['total_tokens']}")
    
    print("\nInput Token Details:")
    for key, value in usage['input_token_details'].items():
        print(f"- {key}: {value}")
    
    print("\nOutput Token Details:")
    for key, value in usage['output_token_details'].items():
        print(f"- {key}: {value}")

if __name__ == "__main__":
    chat_with_usage_tracking()