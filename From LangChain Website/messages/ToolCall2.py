import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
from langchain_core.messages.tool import ToolCall  # Import ToolCall
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

# Function to calculate sum
def calculate_sum(a, b):
    return a + b

# Input values
a = 5
b = 10

# Calculate sum
result = calculate_sum(a, b)

# Create a tool call request to "calculate_sum" with the result
tool_request = ToolCall(
    name="calculate_sum",  # The tool we want to call
    args={"a": a, "b": b, "result": result},  # Pass the result too
    id="sum_001"  # Unique identifier for tracking
)

# Simulate an AI response using AIMessage
ai_response = AIMessage(
    content=f"The sum of {a} and {b} is {result}.",
    tool_calls=[tool_request]
)


# Print the AI's tool request
print("AI Requesting Tool Call:", ai_response)


print("\nThis is the AI or the LLM Calls\n")

# Actually send a message to the AI
response = llm.invoke(f"What is the result{ai_response}")

print("AI Response:", response.content)


