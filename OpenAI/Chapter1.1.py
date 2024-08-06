#To run this you need openai api key

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
)

response = llm.invoke("Write a poem about AI")

print(response)
