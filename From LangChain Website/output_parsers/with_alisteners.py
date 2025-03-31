# ERROR
"""
14. with_alisteners() - Add Async Listeners for Monitoring
This method adds event listeners that trigger actions asynchronously.
"""

import asyncio
from langchain_groq import ChatGroq

async def listener(event):
    print("\n=== with_alisteners() Event ===")
    print(f"Received event: {event}")

llm = ChatGroq(model="llama-3.3-70b-versatile").with_alisteners([listener])

async def main():
    response = await llm.ainvoke("What is the future of AI?")
    print(response)

asyncio.run(main())

