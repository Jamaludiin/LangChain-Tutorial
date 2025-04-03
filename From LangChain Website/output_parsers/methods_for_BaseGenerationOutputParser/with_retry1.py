

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize Groq Chat Model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,  # This is separate from with_retry()
)

# Enable automatic retries
llm_with_retry = llm.with_retry(
    retry_if_exception_type=(Exception,),  # Retry on any exception
    stop_after_attempt=3,  # Retry up to 3 times
    wait_exponential_jitter=True,  # Add random delay between retries
)

# Invoke a request with retry enabled
try:
    response = llm_with_retry.invoke("Explain blockchain in simple terms.")
    print("\n=== with_retry() Response ===")
    print(response.content)
except Exception as e:
    print("\n=== Error ===")
    print(str(e))
