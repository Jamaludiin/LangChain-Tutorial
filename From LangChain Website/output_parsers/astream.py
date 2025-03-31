"""
5. astream() - Stream Output Asynchronously
This method streams responses in real time.
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
    max_tokens=200,
    timeout=10,
    max_retries=2,
)

async def main():
    print("\n=== astream() Response ===")
    async for chunk in llm.astream("Tell me a short story about AI."):
        print(chunk, end="")

# Run the async function
asyncio.run(main())
