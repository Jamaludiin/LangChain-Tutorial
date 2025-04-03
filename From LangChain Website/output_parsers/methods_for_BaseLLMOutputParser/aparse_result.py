# error

import os
from dotenv import load_dotenv
from langchain_core.output_parsers.base import BaseLLMOutputParser
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Set up the Groq LLM
groq_api_key = os.getenv('GROQ_API_KEY')
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define a simple synchronous response parser with the parse_result method
class AsyncResponseParser(BaseLLMOutputParser):
    async def aparse_result(self, result: list, *, partial: bool = False):
        """Asynchronously process the results."""
        if not result:
            return "No response generated."

        # Print the structure of the result for debugging
        print("Response structure:", result)

        # Check if it's a list of dictionaries containing the 'text' field
        if isinstance(result[0], dict) and 'text' in result[0]:
            return f"Asynchronous result: {result[0]['text'].strip()}"
        else:
            return "Unexpected response format."

def main():
    prompt = "Describe the impact of artificial intelligence on society."
    messages = [HumanMessage(content=prompt)]  # Wrap the prompt inside HumanMessage

    # Generate response using the Groq model
    response = llm.generate([messages])  # This is now used synchronously

    # Parse the response synchronously
    parser = AsyncResponseParser()
    parsed_sync_response = parser.aparse_result(response.generations)  # Direct call without 'await'

    # Print the parsed result
    print("Parsed async response:", parsed_sync_response)

# Run the main function
main()
