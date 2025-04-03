
# working
"""19. with_types() - Enforce Output Type (JSON, Text, etc.)
This method ensures the response follows a specific type.
"""

"""
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile")

# Force JSON output
llm_json = llm.with_types({"output": "json"})

response = llm_json.invoke("Describe a cat in JSON format.")

print("\n=== with_types() Response ===")
print(response)"""

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model with the API key
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,  # Added API key explicitly
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define expected output structure
class CatDescription(TypedDict):
    name: str
    color: str
    breed: str
    personality: str

# Bind the output type to enforce JSON format
llm_json = llm.with_types(output_type=CatDescription)

# Invoke with a structured response request
response = llm_json.invoke("Provide a JSON description of a cat including name, color, breed, and personality.")

print("\n=== with_types() Response ===")
print(response.content)



"""
No, defining CatDescription is not compulsory, but it helps enforce structured output when using with_types().

Alternative Without CatDescription
If you don’t want to define a TypedDict, you can use a generic Python dict instead:
"""

llm_json = llm.with_types(output_type=dict)

response = llm_json.invoke("Provide a JSON description of a cat including name, color, breed, and personality.")

print("\n=== with_types() Response ===")
print(response)
