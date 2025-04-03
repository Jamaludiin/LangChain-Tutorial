"""
9. bind() - Predefine Parameters for Future Calls
This method binds parameters to reuse them in multiple LLM calls.
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

# Bind common parameters
llm_bound = llm.bind(temperature=0.5, max_tokens=50)

# Call with predefined parameters
response = llm_bound.invoke("Explain machine learning in one sentence.")

print("\n=== bind() Response ===")
print(response.content)
