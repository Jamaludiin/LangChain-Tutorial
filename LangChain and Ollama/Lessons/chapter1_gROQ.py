

# let me use groq since the olama is heavy and slow
import os
from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv  # Add this import

load_dotenv()  # Add this line

# Get API key and validate
groq_api_key = os.getenv('GROQ_API_KEY')
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set")

# Initialize Groq client and LLM
# Load .env file

# Get API key and validate
groq_api_key = os.getenv('GROQ_API_KEY')


client = Groq(api_key=groq_api_key)
groq_llm = ChatGroq(
    #model="mixtral-8x7b-32768",
    model="llama-3.3-70b-versatile",

    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Get response from Groq
response = groq_llm.invoke("Write a poem about AI")
print("\n")
print(response.content)
print("\n")
