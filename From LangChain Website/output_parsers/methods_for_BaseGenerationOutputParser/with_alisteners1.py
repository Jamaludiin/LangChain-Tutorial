

import os
import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Define async event listeners
async def on_start(event):
    print("\n=== AI Request Started ===")
    print(f"Request Details: {event}")

async def on_end(event):
    print("\n=== AI Request Completed ===")
    print(f"Response Details: {event}")

async def on_error(event):
    print("\n=== AI Request Failed ===")
    print(f"Error Details: {event}")

# Initialize the Groq chat model with async listeners
llm = ChatGroq(model="llama-3.3-70b-versatile").with_listeners({
    "on_start": on_start,
    "on_end": on_end,
    "on_error": on_error
})

# Async function to call AI model
async def main():
    response = await llm.ainvoke("What is the future of AI?")
    print("\n=== AI Response ===")
    print(response)

# Run the async function
asyncio.run(main())
