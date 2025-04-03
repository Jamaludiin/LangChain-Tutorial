# ERROR

"""16. with_fallbacks() - Provide Alternative Models if Primary Fails
This method automatically switches to a fallback model if the main model fails.
"""

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.3-70b-versatile")

# Define fallback models
llm_fallback = llm.with_fallbacks(["mixtral-8x7b", "gemini-pro"])

response = llm_fallback.invoke("What is the meaning of life?")

print("\n=== with_fallbacks() Response ===")
print(response)