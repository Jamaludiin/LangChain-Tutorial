# WORKING

"""from dotenv import load_dotenv
load_dotenv()"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.llms import Ollama

# Instantiate Model
llm = ollama_llm = Ollama(
    model="llama2",
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
print(response)