#To run this you need openai api key

from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

llm = ChatGroq(
    model="mixtral-8x7b-32768",
)


response = llm.invoke("Write a poem about AI")

print(response) # unstructured output 
print("\n", response.content)

