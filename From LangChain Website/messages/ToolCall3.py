import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from langchain_core.messages.tool import ToolCall  # Import ToolCall

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Ensure API key is set
if not groq_api_key:
    raise ValueError("Missing GROQ_API_KEY. Please set it in the environment variables.")

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=500,  # Adjusted max tokens for better efficiency
    timeout=10,
    max_retries=2,
)

# Function to calculate sum
def calculate_sum(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Define input values
a = 5
b = 10

# Calculate sum
result = calculate_sum(a, b)

# Create a tool call request to "calculate_sum" with the result
tool_request = ToolCall(
    name="calculate_sum",  
    args={"a": a, "b": b, "result": result},  
    id="sum_001"  
)

# Simulate an AI response with the tool request
ai_response = AIMessage(
    content=f"Calling tool 'calculate_sum' with a={a}, b={b}.",
    tool_calls=[tool_request]
)

# Print the AI's tool request
print("AI Requesting Tool Call:\n", ai_response.content)

# Actually send a message to the AI and get a response
query = f"What is {a} + {b}?"
response = llm.invoke(query)

# Print AI's final response
print("\nAI Response:", response.content)
