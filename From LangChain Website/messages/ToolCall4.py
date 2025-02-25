import os
from dotenv import load_dotenv
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.messages.tool import ToolCall

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

# Step 1: Send a request to the AI to ask for a calculation
user_request = HumanMessage(content="Please calculate the sum of 7 and 3.")

# Step 2: Invoke the AI model
ai_response = llm.invoke([user_request])

# Step 3: Check if the AI requested a tool call
if ai_response.tool_calls:
    for tool_call in ai_response.tool_calls:
        if tool_call.name == "calculate_sum":
            # Extract arguments and compute result
            a = tool_call.args.get("a")
            b = tool_call.args.get("b")
            result = calculate_sum(a, b)

            # Step 4: Respond back with the calculated result
            tool_result = AIMessage(
                content=f"The sum of {a} and {b} is {result}.",
                tool_calls=[
                    ToolCall(
                        name="calculate_sum",
                        args={"a": a, "b": b, "result": result},
                        id=tool_call.id,
                    )
                ],
            )

            # Send the result back to the AI
            final_response = llm.invoke([tool_result])

            print("\n✅ Final AI Response:", final_response.content)

else:
    print("\n❌ No tool call was requested by the AI.")
