
import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import FunctionMessage
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

# Simulating a function execution and sending the result back
function_result = FunctionMessage(
    content="The current temperature in New York is 22°C.",
    name="get_weather_info"
)

# Print function execution result
print("Function Name:", function_result.name)
print("Function Result:", function_result.content)
