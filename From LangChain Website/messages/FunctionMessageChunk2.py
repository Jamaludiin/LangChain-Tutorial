
import os
from langchain_groq import ChatGroq
from langchain_core.messages import FunctionMessageChunk, AIMessage
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

# Simulated function to fetch weather data
def get_weather_info(city):
    """Mock function that returns weather details."""
    weather_data = {
        "New York": "22°C, Sunny",
        "London": "18°C, Cloudy",
        "Tokyo": "25°C, Clear Sky"
    }
    return weather_data.get(city, "Weather data not available")

# User input (this would typically come from an LLM response)
user_query = "What is the weather like in New York?"

# Pass the query to the LLM to extract the city name
llm_response = llm.invoke(user_query)

# Simulated city extraction from LLM (in a real case, use NLP parsing)
city = "New York" if "New York" in llm_response.content else "Unknown"

# Fetch the weather information
weather_result = get_weather_info(city)

# Create a FunctionMessageChunk with the function output
function_message = FunctionMessageChunk(
    content=f"The current weather in {city} is {weather_result}.",
    name="get_weather_info"
)

# Display AI response and function result
print("LLM Response:", llm_response.content)
print("Function Name:", function_message.name)
print("Function Result:", function_message.content)

# Pretty representation of the function message
pretty_output = function_message.pretty_repr()
print("\nPretty Output:\n", pretty_output)
