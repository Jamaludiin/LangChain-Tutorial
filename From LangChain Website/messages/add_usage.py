import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessageChunk
from langchain_core.messages.ai import add_usage, UsageMetadata, InputTokenDetails, OutputTokenDetails
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

# Simulating UsageMetadata for API calls
usage_1 = UsageMetadata(
    input_tokens=5,
    output_tokens=0,
    total_tokens=5,
    input_token_details=InputTokenDetails(cache_read=3)
)

usage_2 = UsageMetadata(
    input_tokens=0,
    output_tokens=10,
    total_tokens=10,
    output_token_details=OutputTokenDetails(reasoning=4)
)

# Add usage statistics together
total_usage = add_usage(usage_1, usage_2)

# Print the combined usage metadata
print("Combined Usage Metadata:", total_usage)


#----------------------------
response = llm.invoke("Give me the result of 2+3")
print("\nLLM RESPONSE")
print(response)

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


"""
Why is input_tokens = 44?
When you send a prompt like:


"Give me the result of 2+3"
it does not directly translate to 44 tokens. Instead, the following factors contribute:

System Messages & Metadata:
    Many LLMs include hidden system instructions like "You are a helpful assistant."
    Some models add structured metadata such as "format your response as plain text."
    LangChain might also send additional context for better responses.

Why is total_tokens = 52?
Total tokens are calculated as:

\text{total_tokens} = \text{input_tokens} + \text{output_tokens}
Given that:
    input_tokens = 44
    output_tokens = 8
\text{total_tokens} = 44 + 8 = 52
"""