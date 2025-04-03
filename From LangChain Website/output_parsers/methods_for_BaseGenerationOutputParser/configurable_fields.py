"""
11. configurable_fields() - View Configurable Fields
This method lists all configurable parameters available for an LLM instance.
"""

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile")

# Get configurable fields
fields = llm.configurable_fields()
print("\n=== configurable_fields() ===")
print(fields)
