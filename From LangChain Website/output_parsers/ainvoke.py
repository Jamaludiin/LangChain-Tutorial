"""
3. ainvoke() - Run a Single Prompt Asynchronously
This method runs a single prompt asynchronously.
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
    response = await llm.ainvoke("Who is the CEO of Tesla?")
    print("\n=== ainvoke() Response ===")
    print(response.content)

# Run the async function
asyncio.run(main())
