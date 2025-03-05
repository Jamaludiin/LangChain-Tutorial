import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import FunctionMessageChunk
from langchain_core.messages.tool import default_tool_chunk_parser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Example raw tool calls (mock data)
raw_tool_calls = [
    {"name": "sum_numbers", "arguments": {"a": 5, "b": 10}},
    {"name": "multiply_numbers", "arguments": {"x": 3, "y": 4}},
]

# Parse the tool call chunks
parsed_tool_calls = default_tool_chunk_parser(raw_tool_calls)

# Print the parsed output
for tool_call in parsed_tool_calls:
    print(tool_call)



"""
Why Use default_tool_chunk_parser?
default_tool_chunk_parser is used to process and structure tool call responses that come in a raw dictionary format.

🔹 Main Reasons for Using It:
    Standardizing Responses:
        When a model like Groq calls a tool (e.g., fetching weather data, performing calculations), the response comes as raw dictionaries.
        default_tool_chunk_parser ensures that the tool call responses are formatted correctly into ToolCallChunk objects.
    
    Easier Handling of Tool Outputs:
        Instead of manually parsing dictionaries, this method automatically extracts relevant fields and converts them into structured objects.
        Makes it easier to access function names, arguments, and responses.
    
    Best-Effort Parsing:
        It tries its best to parse tool responses, even if they are not perfectly structured.
        Helps prevent errors when dealing with API responses.

        
🔹 Example Use Case
Imagine you're building a chatbot that can call external tools for performing tasks like calculations or retrieving information.

✅ Without default_tool_chunk_parser (Manual Parsing)

raw_tool_calls = [
    {"name": "sum_numbers", "arguments": {"a": 5, "b": 10}},
]

# Manual parsing
for tool in raw_tool_calls:
    tool_name = tool["name"]
    tool_args = tool["arguments"]
    print(f"Calling tool: {tool_name} with args {tool_args}")

👉 Issue: You manually extract values, which can be error-prone if the structure changes.

✅ With default_tool_chunk_parser   
from langchain_core.messages.tool import default_tool_chunk_parser

parsed_tool_calls = default_tool_chunk_parser(raw_tool_calls)
print(parsed_tool_calls)
👉 Advantage: Returns properly structured objects that are easier to use in LangChain.

🔹 When Should You Use It?
✅ When processing responses from tool calls in LangChain
✅ When working with AI agents that use external tools
✅ When you need structured tool call outputs

🔹 Final Thoughts
Instead of manually handling dictionaries, default_tool_chunk_parser makes tool call responses more structured and reliable. It’s useful for AI-powered applications that call external tools dynamically. 🚀
"""