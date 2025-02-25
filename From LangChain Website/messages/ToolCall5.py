# ERROR BUT IDEA IS GOOD

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.tools import StructuredTool
from pydantic.v1 import BaseModel, Field  # Ensure Pydantic v1 for compatibility

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2
)

# Step 1: Define a Pydantic schema for the tool input
class SumInput(BaseModel):
    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")

# Step 2: Define the function with structured input
def calculate_sum(input: SumInput) -> int:
    """Calculates the sum of two integers and returns the result."""
    return input.a + input.b

# Step 3: Register the tool using `StructuredTool`
calculate_sum_tool = StructuredTool.from_function(
    func=calculate_sum,
    name="calculate_sum",
    description="Calculates the sum of two numbers. Provide two integers as inputs."
)

# Step 4: Provide system instruction
system_prompt = SystemMessage(
    content="You are an AI that can use tools. Use the `calculate_sum` tool whenever a user asks for a sum."
)

# Step 5: User request
user_request = HumanMessage(content="What is the sum of 7 and 3?")

# Step 6: Invoke LLM with the tool
ai_response = llm.invoke(
    [system_prompt, user_request],
    tools=[calculate_sum_tool]  # ✅ Now properly registered
)

# Step 7: Check if the AI requested a tool call
if ai_response.tool_calls:
    for tool_call in ai_response.tool_calls:
        if tool_call.name == "calculate_sum":
            # Parse arguments using Pydantic
            input_data = SumInput(**tool_call.args)
            result = calculate_sum(input_data)  # Execute function

            # Provide tool output back to LLM
            tool_result = AIMessage(
                content=f"The sum of {input_data.a} and {input_data.b} is {result}.",
            )

            # Final AI response
            final_response = llm.invoke([tool_result])
            print("\n✅ Final AI Response:", final_response.content)
else:
    print("\n❌ No tool call was requested by the AI.")
