
# This method processes multiple prompts in parallel asynchronously.


"""
1. abatch() - Run Multiple Prompts Asynchronously
This method processes multiple prompts in parallel asynchronously.
"""
import os
import asyncio
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

async def main():
    prompts = [
        "Tell me a joke",
        "Who discovered gravity?",
        "Explain quantum computing in one sentence"
    ]
    
    responses = await llm.abatch(prompts)

    print("\n=== abatch() Responses ===")
    for i, response in enumerate(responses):
        print(f"\nPrompt {i+1}: {prompts[i]}")
        print(f"Response: {response.content}")

# Run the async function
asyncio.run(main())
