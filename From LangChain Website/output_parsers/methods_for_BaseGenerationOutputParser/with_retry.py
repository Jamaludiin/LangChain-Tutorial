# ERROR

"""18. with_retry() - Automatically Retry Failed Calls
This method retries requests in case of failure.
"""

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile")

# Enable retries
llm_retry = llm.with_retry(max_retries=3)

response = llm_retry.invoke("Explain blockchain in simple terms.")

print("\n=== with_retry() Response ===")
print(response)
