
"""
15. with_config() - Set Custom Configuration for Calls
This method customizes settings like retries, caching, and more.
"""

import os
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableConfig  # Ensure correct import
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define custom configuration
custom_config = RunnableConfig(config={"temperature": 0.2, "max_tokens": 50})

# Apply custom configuration
llm_custom = llm.with_config(custom_config)

# Invoke with custom settings
try:
    response = llm_custom.invoke("Summarize the history of the internet in 50 words.")
    print("\n=== with_config() Response ===")
    print(response.content)
except Exception as e:
    print("\n=== Error ===")
    print(str(e))



"""
The .with_config() method in LangChain allows you to bind a custom configuration to a Runnable, returning a new instance with the updated settings.

🔹 What .with_config() Does
Modifies parameters without changing the original model instance.

Allows setting custom configurations dynamically, such as:

    temperature (randomness in responses)

    max_tokens (limits response length)

    timeout (request timeout duration)

    max_retries (number of retries on failure)

    Other model-specific settings.

✅ Example Use Case
    Imagine you have an AI model that generates responses.
    You normally use this:


    llm.invoke("Tell me about quantum computing.")
    But now, you want to customize settings for a specific call:


    llm_custom = llm.with_config({"temperature": 0.2, "max_tokens": 50})
    response = llm_custom.invoke("Summarize quantum computing.")

This will:
    Reduce randomness (temperature=0.2) → Makes responses more consistent.

    Limit response length (max_tokens=50) → Keeps it brief.

🛠 How It Works Internally
    Creates a new Runnable with the provided config.

    Doesn’t modify the original llm instance.

    Overrides settings only for that instance.

This is useful when you need different configurations for different tasks without affecting the main model setup.

"""