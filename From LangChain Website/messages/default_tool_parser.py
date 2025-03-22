import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages.tool import default_tool_parser

# Load environment variables
from dotenv import load_dotenv
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

# Sample raw tool call responses (some valid, some invalid)
raw_tool_calls = [
    {"name": "sum_numbers", "arguments": {"a": 5, "b": 10}},  # ✅ Valid
    {"name": "get_weather", "arguments": {"city": "New York"}},  # ✅ Valid
    {"wrong_key": "invalid_data"}  # ❌ Invalid
]

# Parse the tool calls using default_tool_parser
valid_calls, invalid_calls = default_tool_parser(raw_tool_calls)

# Print the results
print("✅ Valid Tool Calls:")
for call in valid_calls:
    print(call)

print("\n❌ Invalid Tool Calls:")
for call in invalid_calls:
    print(call)



"""
🔹 Explanation
We define a list of tool calls (raw_tool_calls).
    Some are correctly structured (e.g., sum_numbers, get_weather).
    Some are incorrectly structured (wrong_key).
default_tool_parser processes the tool calls and returns:
    ✅ Valid tool calls (properly structured)
    ❌ Invalid tool calls (incorrectly structured)
We print the valid and invalid tool calls separately.


🔹 Why Use This?
✅ Automatically filters out incorrect tool calls
✅ Helps AI handle API tool responses reliably
✅ Avoids manual dictionary parsing

This is useful when working with AI agents that call external tools dynamically. 🚀
"""


"""
Difference Between default_tool_chunk_parser and default_tool_parser
Both methods process raw tool call data, but they have key differences in functionality and output.

1️⃣ default_tool_chunk_parser
📌 Purpose:

Processes tool chunks (partial tool calls).
Returns a list of tool call chunks.
📌 Output:

list[ToolCallChunk] → A list of processed tool call chunks.
✅ Best when handling partial responses from AI models.

🔹 Example Use Case:
If an AI model is streaming its output and hasn't completed a full tool call, this method helps extract whatever partial tool call is available.

2️⃣ default_tool_parser
📌 Purpose:

Processes full tool calls.
Separates valid and invalid tool calls.
📌 Output:

tuple[list[ToolCall], list[InvalidToolCall]]
✅ Valid tool calls (ToolCall)
❌ Invalid tool calls (InvalidToolCall)
✅ Best when handling complete tool call responses and filtering out bad tool calls.

🔹 Example Use Case:
When an AI model generates multiple complete tool calls, this method helps separate good from bad before execution.

🔍 Summary: Key Differences
Feature	default_tool_chunk_parser	default_tool_parser
Processes	Partial tool call chunks	Full tool calls
Handles Streaming	✅ Yes	❌ No
Separates Valid & Invalid Calls	❌ No	✅ Yes
Best For	Handling AI responses that are incomplete	Filtering full tool call responses
🚀 When to Use Which?
If working with partial tool call responses → 🟢 Use default_tool_chunk_parser
If working with complete tool call responses → 🟢 Use default_tool_parser

"""