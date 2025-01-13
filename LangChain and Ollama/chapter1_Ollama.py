# WORKING

from langchain.llms import Ollama

ollama_llm = Ollama(
    model="llama2",
)

response = ollama_llm.invoke("Write a poem about AI")

print (response)