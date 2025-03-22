import os
from langchain_groq import ChatGroq
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

# Send a request to the model
response = llm.invoke("Give me the result of 2+3")

# Accessing the token usage details
token_usage = response.response_metadata['token_usage']

# Print each detail one by one
print("Prompt Tokens:", token_usage['prompt_tokens'])
print("Completion Tokens:", token_usage['completion_tokens'])
print("Total Tokens:", token_usage['total_tokens'])
print("Completion Time:", token_usage['completion_time'])
print("Prompt Time:", token_usage['prompt_time'])
print("Queue Time:", token_usage['queue_time'])
print("Total Time:", token_usage['total_time'])

# Print additional metadata
print("Model Name:", response.response_metadata['model_name'])
print("System Fingerprint:", response.response_metadata['system_fingerprint'])
print("Finish Reason:", response.response_metadata['finish_reason'])
