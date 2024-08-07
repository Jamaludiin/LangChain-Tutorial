from langchain_community.llms import Ollama

ollama = Ollama(
    base_url='http://localhost:11434', # this is the port ollama running in your local machine. Output will be if u visit this: Ollama is running
    model="llama3"
)

print(ollama.invoke("why is the sky blue"))