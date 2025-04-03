
"""
2. Import Required Modules

Begin by importing the necessary modules:
"""

from langchain_core.output_parsers.base import BaseLLMOutputParser
from langchain_core.outputs import Generation


import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
"""
3. Set Up the Groq Chat Model

Initialize the Groq chat model with your API key and desired parameters:
"""


# Load environment variables
load_dotenv()


groq_api_key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=32767,
        timeout=10,
        max_retries=2,
    )

"""
4. Define a Custom Output Parser

Create a custom parser by subclassing BaseLLMOutputParser. This parser will process the raw output from the LLM:
"""
class SimpleResponseParser(BaseLLMOutputParser):
    def parse_result(self, result: list[Generation], *, partial: bool = False):
        # Select the first generation's text
        return result[0].text.strip()





"""
5. Generate and Parse a Response

Now, you can generate a response using the chat model and parse it with your custom parser:
"""
# Define the input prompt
prompt = "Hello, how can I assist you today?"

# Generate a response from the LLM
response = llm.invoke(prompt)

# Parse the response using the custom parser
parser = SimpleResponseParser()
parsed_response = parser.parse_result([Generation(text=response.content)])

# Output the parsed response
print(parsed_response)
