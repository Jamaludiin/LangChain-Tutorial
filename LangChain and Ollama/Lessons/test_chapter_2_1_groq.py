# WORKING


from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

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



# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Generate a list of 10 synonyms for the following word. Return the results as a comma seperated list."),
        ("human", "{input}")
    ]
)

# Create LLM Chain
chain = prompt | llm

response = chain.invoke({"input": "happy"})
print("\n")
print(response.content)
print("\n")
