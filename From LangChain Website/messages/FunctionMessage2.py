# working
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

# Define the function
def get_weather_info(city):
    """Mock function to simulate fetching weather info."""
    weather_data = {
        "New York": "22°C, Sunny",
        "London": "18°C, Cloudy",
        "Tokyo": "25°C, Clear Sky"
    }
    return weather_data.get(city, "Weather data not available")

# Call the function
city = "New York"
weather_result = get_weather_info(city)

# Create FunctionMessage with actual function output
function_result = FunctionMessage(
    content=f"The current temperature in {city} is {weather_result}.",
    name="get_weather_info"
)

# Print function execution result
print("Function Name:", function_result.name)
print("Function Result:", function_result.content)
