import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import FunctionMessageChunk
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

# Define a function that simulates fetching weather info
def get_weather_info(city):
    """Mock function to return weather details."""
    weather_data = {
        "New York": "22°C, Sunny",
        "London": "18°C, Cloudy",
        "Tokyo": "25°C, Clear Sky"
    }
    return weather_data.get(city, "Weather data not available")

# Call the function with an example city
city = "New York"
weather_result = get_weather_info(city)

# Create a FunctionMessageChunk with the function output
function_message = FunctionMessageChunk(
    content=f"The current weather in {city} is {weather_result}.",
    name="get_weather_info"
)

# Print the function message output
print("Function Name:", function_message.name)
print("Function Result:", function_message.content)

# Get a pretty representation of the message
pretty_output = function_message.pretty_repr()
print("\nPretty Output:\n", pretty_output)
