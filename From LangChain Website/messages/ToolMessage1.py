import os
import datetime
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import ToolMessage, HumanMessage, AIMessage
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

# Function to calculate age
def calculate_age(birth_year: int) -> int:
    current_year = datetime.datetime.now().year
    return current_year - birth_year

# Simulated user question
user_message = HumanMessage(content="What is my age if I was born in 1995?")

# AI recognizes a tool call (this would be extracted from LLM response in a real case)
birth_year = 1995  # Extracted from user input
tool_call_id = "call_age_001"  # Unique ID for this tool execution

# Execute the age calculation
age_result = calculate_age(birth_year)

# Send the tool execution result back to the model
tool_message = ToolMessage(
    content=str(age_result),  # Send the calculated age as a string
    tool_call_id=tool_call_id
)

# AI model receives the tool output and formulates a response
ai_response = AIMessage(content=f"You are {age_result} years old.")

# Print the AI's response
print(ai_response.content)
