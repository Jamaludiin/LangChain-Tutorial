"""
2. abatch_as_completed() - Process Responses as They Complete
This method returns responses as soon as they complete, rather than waiting for all responses to finish.
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
        "What is the capital of Japan?",
        "Who wrote '1984'?",
        "Translate 'hello' to Spanish"
    ]

    print("\n=== abatch_as_completed() Responses ===")
    async for response in llm.abatch_as_completed(prompts):
        print(response)

# Run the async function
asyncio.run(main())
