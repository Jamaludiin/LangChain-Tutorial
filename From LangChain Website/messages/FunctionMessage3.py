

# If you want to define get_weather_info but still use the Groq LLM to generate the weather information dynamically, you can do it like this:

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
    max_tokens=100,
    timeout=10,
    max_retries=2,
)

# Define the function to get weather information using LLM
def get_weather_info(city):
    """Fetches weather information using Groq LLM."""
    query = f"What is the weather like in {city}?"
    response = llm.invoke(query)
    return response.content  # Return the generated weather info

# Call the function with a city name
city = "New York"
weather_result = get_weather_info(city)

# Create a FunctionMessage with the function output
function_result = FunctionMessage(
    content=f"The current weather in {city} is: {weather_result}",
    name="get_weather_info"
)

# Print the result
print("Function Name:", function_result.name)
print("Function Result:", function_result.content)
