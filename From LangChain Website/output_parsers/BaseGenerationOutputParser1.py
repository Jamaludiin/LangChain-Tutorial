from langchain_core.output_parsers import BaseOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Define a custom output parser
class JSONOutputParser(BaseOutputParser):
    def parse(self, text: str):
        """Parses LLM output into a structured dictionary."""
        import json
        try:
            return json.loads(text)  # Convert string output to a Python dictionary
        except json.JSONDecodeError:
            return {"error": "Invalid JSON output"}



# Define a structured prompt
prompt = ChatPromptTemplate.from_template(
    "Provide a JSON object with a 'question' and 'answer' field for the topic: {topic}"
)

# Generate response
formatted_prompt = prompt.format(topic="Artificial Intelligence")
response = llm.invoke(formatted_prompt)

# Parse response
parser = JSONOutputParser()
parsed_output = parser.parse(response.content)

print(parsed_output)
