# ERROR

"""
15. with_config() - Set Custom Configuration for Calls
This method customizes settings like retries, caching, and more.
"""

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile")

# Configure with custom settings
llm_custom = llm.with_config({"temperature": 0.2, "max_tokens": 50})

response = llm_custom.invoke("Summarize the history of the internet in 50 words.")

print("\n=== with_config() Response ===")
print(response)
