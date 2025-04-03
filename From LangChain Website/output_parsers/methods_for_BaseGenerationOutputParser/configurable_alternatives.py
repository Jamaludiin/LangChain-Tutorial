# ERROR
"""
10. configurable_alternatives() - Set Alternative Configurations
This method allows switching between multiple predefined configurations dynamically.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=100,
    timeout=10,
    max_retries=2,
)


# Define alternative configurations
configs = llm.configurable_alternatives("temperature", [0.2, 0.7, 1.0])

for config in configs:
    print("\n=== configurable_alternatives() Response ===")
    print(config.invoke("Tell me a creative idea for a startup."))
  
