
# ERROR
"""19. with_types() - Enforce Output Type (JSON, Text, etc.)
This method ensures the response follows a specific type.
"""


import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

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



"""
No, defining CatDescription is not compulsory, but it helps enforce structured output when using with_types().

Alternative Without CatDescription
If you don’t want to define a TypedDict, you can use a generic Python dict instead:
"""

llm_json = llm.with_types(output_type=dict)

response = llm_json.invoke("Provide a JSON description of a cat including name, color, breed, and personality.")

print("\n=== with_types() Response ===")
print(response)
