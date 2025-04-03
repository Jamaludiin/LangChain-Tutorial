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

# Define a simple output parser with the parse_result method
class SimpleResponseParser(BaseLLMOutputParser):
    def parse_result(self, result: list, *, partial: bool = False):
        """Synchronously process the results."""
        if not result:
            return "No response generated."
        
        # Print the structure of the result for debugging
        print("Response structure:", result)
        
        # Check the type and structure of the result before processing
        if isinstance(result[0], dict) and 'text' in result[0]:  # If it's a list of dictionaries
            return f"Synchronous result: {result[0]['text'].strip()}"
        else:
            return "Unexpected response format."

def main():
    prompt = "Describe the impact of artificial intelligence on society."
    messages = [HumanMessage(content=prompt)]  # Wrap the prompt inside HumanMessage

    # Send the message to the Groq model and get the response synchronously
    response = llm.generate([messages])  # No need to await, it's a synchronous method

    # Parsing the response synchronously
    parser = SimpleResponseParser()
    parsed_sync_response = parser.parse_result(response.generations)
    print("Parsed sync response:", parsed_sync_response)  # Print the synchronous result

# Run the main function
main()
