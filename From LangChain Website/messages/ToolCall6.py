import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.tools import Tool
from pydantic import BaseModel, Field

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# ✅ Initialize the LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2
)

# ✅ Step 1: Define a Pydantic schema for tool input
class SumInput(BaseModel):
    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")

# ✅ Step 2: Define the function
def calculate_sum(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b

# ✅ Step 3: Register the tool with `args_schema`
calculate_sum_tool = Tool(
    name="calculate_sum",
    func=calculate_sum,
    description="Calculates the sum of two integers.",
    args_schema=SumInput  # ✅ Properly structured with Pydantic
)

# ✅ Step 4: Provide system instruction
system_prompt = SystemMessage(
    content="You are an AI that can use tools. Use the `calculate_sum` tool whenever a user asks for a sum."
)

# ✅ Step 5: User request
user_request = HumanMessage(content="What is the sum of 7 and 3?")

# ✅ Step 6: Invoke LLM with tool usage enabled
try:
    ai_response = llm.invoke(
        [system_prompt, user_request],
        tools=[calculate_sum_tool]  # ✅ Proper tool registration
    )

    # ✅ Step 7: Check if the AI requested a tool call
    if ai_response.tool_calls:
        for tool_call in ai_response.tool_calls:
            if tool_call.name == "calculate_sum":
                # ✅ Parse arguments using Pydantic
                input_data = SumInput(**tool_call.args)
                result = calculate_sum(input_data.a, input_data.b)  # Execute function

                # ✅ Serialize response properly
                tool_result = AIMessage(
                    content=json.dumps({"sum": result})
                )

                # ✅ Final AI response
                final_response = llm.invoke([tool_result])
                print("\n✅ Final AI Response:", final_response.content)
    else:
        print("\n❌ No tool call was requested by the AI.")

except Exception as e:
    print(f"\n🚨 Error: {e}")
