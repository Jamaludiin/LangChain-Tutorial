# This example simulates tracking input token usage when making a request to the Groq API.
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages.ai import InputTokenDetails
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

# Define a user prompt
user_prompt = "List one benifit of AI that helps businesses automate processes."

# Get AI response
response = llm.invoke(user_prompt)

print("\n", response.content,"\n")
# ✅ Correct way to instantiate InputTokenDetails (it's a TypedDict)
input_token_details: InputTokenDetails = {
    "audio": 10,                # Audio input tokens
    "cache_creation": 200,      # Cache miss tokens
    "cache_read": 100          # Cache hit tokens
}

# 🖨 Print details in a clear format
print("\n🔹 Input Token Breakdown:")
print("🟢 Audio Tokens:", input_token_details["audio"])
print("🟢 Cache Creation Tokens:", input_token_details["cache_creation"])
print("🟢 Cache Read Tokens:", input_token_details["cache_read"])

# Since it's already a dict, no need for .dict() conversion
print("\n🔹 Input Token Details (as dict):")
print(input_token_details)
