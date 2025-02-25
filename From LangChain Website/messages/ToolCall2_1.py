# error fix later
import os
from dotenv import load_dotenv
from datetime import date
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import Tool

# ✅ Load API key from environment
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

# ✅ Define a function to get the current date
def get_current_date():
    """Returns today's date in YYYY-MM-DD format."""
    return date.today().strftime("%Y-%m-%d")

# ✅ Register the function as a LangChain Tool
date_tool = Tool(
    name="get_current_date",
    func=get_current_date,
    description="Returns the current date in YYYY-MM-DD format."
)

# ✅ Provide system instruction
system_prompt = SystemMessage(
    content="You are an AI that can use tools. Use the `get_current_date` tool when asked for today's date."
)

# ✅ User asks for today's date
user_request = HumanMessage(content="What is today's date?")

# ✅ Invoke LLM with tool usage enabled
ai_response = llm.invoke(
    [system_prompt, user_request],
    tools=[date_tool]  # ✅ Register the tool with the LLM
)

# ✅ Check if the AI called the tool
if ai_response.tool_calls:
    for tool_call in ai_response.tool_calls:
        if tool_call.name == "get_current_date":
            result = get_current_date()  # Execute function
            print("\n📅 AI Response:", f"Today's date is {result}.")
else:
    print("\n❌ No tool call was requested by the AI.")
