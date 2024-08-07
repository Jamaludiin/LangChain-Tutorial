from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',

    # required but ignored
    api_key='ollama',
)



completion = client.completions.create(
    model="llama3",
    prompt="Say this is a test",
)

list_completion = client.models.list()

model = client.models.retrieve("llama3")

embeddings = client.embeddings.create(
    model="llama2",
    input=["why is the sky blue?", "why is the grass green?"],
)

print(embeddings)