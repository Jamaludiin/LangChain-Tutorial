from langchain_core.messages.tool import tool_call

# Simulate an AI calling a tool
tool_request = tool_call(
    name="weather_tool",  # AI wants to call this tool
    args={"location": "New York"},  # AI-provided parameters
    id="abc123"  # Optional unique ID for tracking
)

print("Tool Call Request:", tool_request)




#---------------------addtional demon

# Define a weather tool function
def weather_tool(location: str):
    return f"Weather in {location}: Sunny ☀️"

# Tool registry (mapping tool names to actual functions)
tools = {
    "weather_tool": weather_tool
}

# Execute tool dynamically
"""tool_name = tool_request.name  # Extract tool name
tool_args = tool_request.args  # Extract arguments"""
# Access values using dictionary keys
tool_name = tool_request["name"]  # Extract tool name
tool_args = tool_request["args"]  # Extract arguments
tool_id = tool_request["id"]  # Extract ID

if tool_name in tools:
    result = tools[tool_name](**tool_args)  # Call the tool
    print("✅ Tool Result:", result)
else:
    print("❌ Error: Tool not found!")
