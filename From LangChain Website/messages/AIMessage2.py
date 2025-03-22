# This script demonstrates the usage of AIMessage in LangChain
# It remembers past conversations and showcases multiple AIMessage methods.

import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
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

# Define a user prompt
user_prompt = "What are the single benefit of using AI in software development?"

# Get the AI response
response = llm.invoke(user_prompt)

# Create an AIMessage object from the response
ai_message = AIMessage(content=response.content)

# Print AI Message
print("\n🔹 AI Generated Response:")
print(ai_message)
print("-" * 50)

# ---------------------------- MORE METHODS ----------------------------

# 1️⃣ Basic Usage of AIMessage
print("\n🔹 1️⃣ Basic Usage of AIMessage:")
print("🟢 Content:", ai_message.content)
print("-" * 50)

# 2️⃣ response_metadata
ai_message = AIMessage(content="AI response", response_metadata={"token_usage": 50, "model": "llama-3.3-70b"})
print("\n🔹 2️⃣ response_metadata:")
print("🟢 Metadata:", ai_message.response_metadata)
print("-" * 50)

"""
# 3️⃣ usage_metadata
ai_message = AIMessage(content="Sample text", usage_metadata={"tokens_used": 45})
print("\n🔹 3️⃣ usage_metadata:")
print("🟢 Usage Metadata:", ai_message.usage_metadata)
print("-" * 50)
"""


"""# 4️⃣ tool_calls
ai_message = AIMessage(content="Calling an external API", tool_calls=[{"tool": "weather_api", "parameters": {"location": "New York"}}])
print("\n🔹 4️⃣ tool_calls:")
print("🟢 Tool Calls:", ai_message.tool_calls)
print("-" * 50)"""

"""
# 5️⃣ invalid_tool_calls
ai_message = AIMessage(content="Invalid tool usage", invalid_tool_calls=["error: missing parameter"])
print("\n🔹 5️⃣ invalid_tool_calls:")
print("🟢 Invalid Tool Calls:", ai_message.invalid_tool_calls)
print("-" * 50)
"""

# 6️⃣ id
ai_message = AIMessage(content="Hello!", id="msg_12345")
print("\n🔹 6️⃣ id:")
print("🟢 Message ID:", ai_message.id)
print("-" * 50)

# 7️⃣ name (Optional Name Field)
ai_message = AIMessage(content="System update complete.", name="SystemMessage")
print("\n🔹 7️⃣ name:")
print("🟢 Name:", ai_message.name)
print("-" * 50)

# 8️⃣ pretty_print()
ai_message = AIMessage(content=response.content)
print("\n🔹 8️⃣ pretty_print():")
ai_message.pretty_print()
print("-" * 50)

# 9️⃣ pretty_repr(html=False)
print("\n🔹 9️⃣ pretty_repr(html=True):")
print("🟢 HTML Representation:", ai_message.pretty_repr(html=True))
print("-" * 50)
