from dotenv import load_dotenv
load_dotenv()


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


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


# 1: StrOutputParser
def call_string_output_parser():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Tell me a joke about the following subject"),
        ("human", "{input}")
    ])

    parser = StrOutputParser()

    chain = prompt | llm | parser

    return chain.invoke({
        "input": "dog"
    })

# 2: CommaSeparatedListOutputParser
def call_list_output_parser():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate a list of 10 synonyms for the following word. Return the results as a comma seperated list."),
        ("human", "{input}")
    ])

    parser = CommaSeparatedListOutputParser()
    
    chain = prompt | llm | parser

    return chain.invoke({
        "input": "happy"
    })


# 3: JsonOutputParser
def call_json_output_parser():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Extract information from the following phrase.\nFormatting Instructions: {format_instructions}"),
        ("human", "{phrase}")
    ])

    class Person(BaseModel):
        recipe: str = Field(description="the name of the recipe")
        ingredients: list = Field(description="ingredients")
        

    parser = JsonOutputParser(pydantic_object=Person)

    chain = prompt | llm | parser
    
    return chain.invoke({
        "phrase": "The ingredients for a Margherita pizza are tomatoes, onions, cheese, basil",
        "format_instructions": parser.get_format_instructions()
    })


# print(type(call_string_output_parser()))
# print(type(call_list_output_parser()))
print(call_json_output_parser())