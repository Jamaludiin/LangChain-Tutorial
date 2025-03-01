import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages.ai import subtract_usage, UsageMetadata, InputTokenDetails, OutputTokenDetails
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

# Define two UsageMetadata objects
usage_1 = UsageMetadata(
    input_tokens=5,
    output_tokens=10,
    total_tokens=15,
    input_token_details=InputTokenDetails(cache_read=4)
)

usage_2 = UsageMetadata(
    input_tokens=3,
    output_tokens=8,
    total_tokens=11,
    output_token_details=OutputTokenDetails(reasoning=4)
)

# Subtract usage statistics
result_usage = subtract_usage(usage_1, usage_2)

# If result is a dictionary, convert it back to a UsageMetadata object
if isinstance(result_usage, dict):
    result_usage = UsageMetadata(**result_usage)

# Print the result safely
print("Updated Usage Metadata after Subtraction:")
print("Input Tokens:", getattr(result_usage, "input_tokens", 0))
print("Output Tokens:", getattr(result_usage, "output_tokens", 0))
print("Total Tokens:", getattr(result_usage, "total_tokens", 0))

if hasattr(result_usage, "input_token_details") and result_usage.input_token_details:
    print("Cache Read:", getattr(result_usage.input_token_details, "cache_read", 0))

if hasattr(result_usage, "output_token_details") and result_usage.output_token_details:
    print("Reasoning:", getattr(result_usage.output_token_details, "reasoning", 0))


"""
Usage of subtract_usage in LangChain
The subtract_usage function in LangChain is used to subtract two UsageMetadata objects while ensuring that token counts do not become negative.

Why Use subtract_usage?
    Track Token Usage: Helps monitor token consumption by removing previously counted tokens from the total.
    Undo Token Consumption: If an operation is reversed (e.g., undoing a request), subtract_usage helps adjust the token count.
    Compare Token Usage: Allows developers to see how much token usage has changed between two states.
    Ensure Non-Negative Values: Prevents errors caused by negative token counts by enforcing max(left - right, 0).


Example Use Cases
Adjusting Token Usage for Canceled Requests
    If an API call is rolled back or fails, subtract the tokens used in that request from the total usage.

Comparing Token Consumption
    Compare the difference in token usage between two different API calls.

Managing Token Limits
    If an application tracks usage against a budget or limit, subtract_usage helps remove over-reported tokens.   
"""