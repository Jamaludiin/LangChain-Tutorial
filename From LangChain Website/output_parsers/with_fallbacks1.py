import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the main Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,  # Ensure API key is set
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define fallback models
fallback_1 = ChatGroq(model="mixtral-8x7b", api_key=groq_api_key)
fallback_2 = ChatGroq(model="gemini-pro", api_key=groq_api_key)

# Add fallbacks to the primary model
llm_with_fallbacks = llm.with_fallbacks([fallback_1, fallback_2])

# Invoke the model with fallback enabled
try:
    response = llm_with_fallbacks.invoke("What is the meaning of life?")
    print("\n=== with_fallbacks() Response ===")
    print(response.content)
except Exception as e:
    print("\n=== Error ===")
    print(str(e))
