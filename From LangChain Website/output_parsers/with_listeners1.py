

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables.config import RunnableConfig
from typing import Dict, Any

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
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

# Define event listeners
def on_start(run: Dict[str, Any], config: RunnableConfig):
    print("\n=== on_start Event ===")
    print(f"Run Details: {run}")

def on_end(run: Dict[str, Any], config: RunnableConfig):
    print("\n=== on_end Event ===")
    print(f"Run Details: {run}")

def on_error(run: Dict[str, Any], config: RunnableConfig):
    print("\n=== on_error Event ===")
    print(f"Error Details: {run}")

# Bind the listeners to the model
llm_with_listeners = llm.with_listeners(
    on_start=on_start, on_end=on_end, on_error=on_error
)

# Invoke with a sample query
response = llm_with_listeners.invoke("Tell me a fun fact about space.")

print("\n=== Response ===")
print(response.content)



"""
🛠 How It Works
on_start(run, config) → Called before the model starts processing.

Logs Run ID and input text.

on_end(run, config) → Called after the model finishes.

Logs Run ID and output text.

on_error(run, config) → Called if an error occurs.

Logs Run ID and error message.

with_listeners(on_start, on_end, on_error) → Attaches these event listeners to the model.

🔹 Why Use with_listeners()?
✅ Debugging: Helps track API calls and responses.
✅ Logging: You can log errors or performance stats.
✅ Monitoring: Useful in production to monitor API behavior.


"""