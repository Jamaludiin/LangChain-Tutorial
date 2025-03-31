from langchain.schema import BaseGenerationOutputParser
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Define a custom output parser
class MyOutputParser(BaseGenerationOutputParser):
    def parse(self, text: str):
        return text.strip().upper()  # Simple example: Convert text to uppercase

# Initialize LLM and prompt

import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage
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

prompt = PromptTemplate.from_template("Tell me a joke about {topic}.")

# Generate response
response = llm.invoke(prompt.format(topic="programming"))

# Parse response
parser = MyOutputParser()
parsed_output = parser.parse(response)

print(parsed_output)


"""
The BaseGenerationOutputParser class is a base class in 
LangChain used to parse outputs from a Language Model (LLM). 
It provides methods for handling outputs in various ways, including 
batching, streaming, and asynchronous processing.
"""
