
# working

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
user_prompt = "What is the single benefit of using AI in software development?"

# Get the AI response
response = llm.invoke(user_prompt)

# Create an AIMessage object from the response
ai_message = AIMessage(content=response.content)

# Print AI Message
print("\n \n Print AI Message")

print(ai_message)
"""
#----------------------------MORE METHODS--------------

# 1️⃣ Basic Usage of AIMessage

from langchain_core.messages import AIMessage

# Creating an AIMessage instance with content
ai_message = AIMessage(content=response.content)

# Accessing the content of the message
print("\n \n  1️⃣ Basic Usage of AIMessage")
print(ai_message.content)  # Output: "This is an AI-generated response."



# 2️⃣ response_metadata
#Stores metadata about the response, such as headers, token usage, and model-specific details.


ai_message = AIMessage(content="AI response", response_metadata={"token_usage": 50, "model": "llama-3.3-70b"})
print(ai_message.response_metadata)
# Output: {'token_usage': 50, 'model': 'llama-3.3-70b'}


#3️⃣ usage_metadata
# Provides details about resource usage, such as token count.

ai_message = AIMessage(content="Sample text", usage_metadata={"tokens_used": 45})
print(ai_message.usage_metadata)
# Output: {'tokens_used': 45}

# 4️⃣ tool_calls
# Stores any tool calls that the AI model might have generated.


ai_message = AIMessage(content="Calling an external API", tool_calls=[{"tool": "weather_api", "parameters": {"location": "New York"}}])
print(ai_message.tool_calls)
# Output: [{'tool': 'weather_api', 'parameters': {'location': 'New York'}}]

# 5️⃣ invalid_tool_calls
# Captures any tool calls that failed or were improperly parsed.


ai_message = AIMessage(content="Invalid tool usage", invalid_tool_calls=["error: missing parameter"])
print(ai_message.invalid_tool_calls)
# Output: ['error: missing parameter']

# 6️⃣ id
# Stores a unique identifier for the AI-generated message.


ai_message = AIMessage(content="Hello!", id="msg_12345")
print(ai_message.id)
# Output: 'msg_12345'


# 8️⃣ pretty_print()
# Prints a formatted version of the AI message.

ai_message = AIMessage(content="Formatted output")
ai_message.pretty_print()

# 9️⃣ pretty_repr(html=False)
# Returns a formatted representation of the message. If html=True, it outputs an HTML-formatted string.


print(ai_message.pretty_repr(html=True))
"""

"""
Explanation
Initialize ChatGroq: It sets up the Groq chat model (llama-3.3-70b-versatile in this case).
Send a User Prompt: We provide an input (user_prompt).
Invoke the Model: The llm.invoke() function sends the prompt to the model and gets a response.
Store Response in AIMessage: The response is wrapped in an AIMessage instance.
Print the AI Message: Displays the AI's output.

"""


"""
AIMessage Class in LangChain
📌 Key Attributes and Methods
The AIMessage class extends BaseMessage and includes additional fields to manage AI responses effectively.

1️⃣ Basic Usage of AIMessage

from langchain_core.messages import AIMessage

# Creating an AIMessage instance with content
ai_message = AIMessage(content="This is an AI-generated response.")

# Accessing the content of the message
print(ai_message.content)  # Output: "This is an AI-generated response."
2️⃣ response_metadata
Stores metadata about the response, such as headers, token usage, and model-specific details.


ai_message = AIMessage(content="AI response", response_metadata={"token_usage": 50, "model": "llama-3.3-70b"})
print(ai_message.response_metadata)
# Output: {'token_usage': 50, 'model': 'llama-3.3-70b'}
3️⃣ usage_metadata
Provides details about resource usage, such as token count.


ai_message = AIMessage(content="Sample text", usage_metadata={"tokens_used": 45})
print(ai_message.usage_metadata)
# Output: {'tokens_used': 45}
4️⃣ tool_calls
Stores any tool calls that the AI model might have generated.


ai_message = AIMessage(content="Calling an external API", tool_calls=[{"tool": "weather_api", "parameters": {"location": "New York"}}])
print(ai_message.tool_calls)
# Output: [{'tool': 'weather_api', 'parameters': {'location': 'New York'}}]
5️⃣ invalid_tool_calls
Captures any tool calls that failed or were improperly parsed.


ai_message = AIMessage(content="Invalid tool usage", invalid_tool_calls=["error: missing parameter"])
print(ai_message.invalid_tool_calls)
# Output: ['error: missing parameter']
6️⃣ id
Stores a unique identifier for the AI-generated message.


ai_message = AIMessage(content="Hello!", id="msg_12345")
print(ai_message.id)
# Output: 'msg_12345'
7️⃣ name
A human-readable name for the message.


ai_message = AIMessage(content="System update complete.", name="SystemMessage")
print(ai_message.name)
# Output: 'SystemMessage'
8️⃣ pretty_print()
Prints a formatted version of the AI message.


ai_message = AIMessage(content="Formatted output")
ai_message.pretty_print()
Output:


AIMessage(content='Formatted output')
9️⃣ pretty_repr(html=False)
Returns a formatted representation of the message. If html=True, it outputs an HTML-formatted string.


print(ai_message.pretty_repr(html=True))


"""