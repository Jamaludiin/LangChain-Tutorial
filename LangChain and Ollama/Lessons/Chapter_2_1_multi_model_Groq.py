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

"""model = [
    "llama-3.3-70b-versatile",
    "gemma-7b-it", # good but result not formatted in table
    "llama3-8b-8192", # very good consistent results in table.
    "llama3-70b-8192", # very very good consistent results in table.
    "llama-3.2-90b-vision-preview", # VERY GOOD # very good consistent results in table.
    "gemma2-9b-it", # very critical good but result not formatted in table
    "llama-3.1-70b-versatile", # cannot aceess this model.
    "llama-3.1-8b-instant", # 8000 tokens maximum.
    "whisper-large-v3-turbo", # does not support chat completions
         ]"""

# Verify model availability before creating LLM
available_models = [
    "llama-3.3-70b-versatile",
    "gemma-7b-it",
    "llama3-8b-8192",
    "llama3-70b-8192",
    "llama-3.2-90b-vision-preview",
    "gemma2-9b-it"
]

if available_models[0] not in available_models:
    raise ValueError(f"Model {available_models[0]} is not in the list of available models")

try:
    llm = ChatGroq(
        available_models[0],
        temperature=0.7,
        max_tokens=32767,
        timeout=10,
        max_retries=2,
    )
except Exception as e:
    print(f"Error initializing Groq model: {str(e)}")
    raise


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
