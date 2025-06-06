# working

from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    base_url='http://localhost:11434/v1/',  # Ollama server URL
    api_key='ollama',  # Required but ignored for local use
)

# Define the prompt/question you want to ask
prompt = "What is component design, and why is it important in software development?"

# Function to send the prompt and get the response

response = client.completions.create(
    model="llama3",  # Specify the model you want to use
    prompt=prompt,
    max_tokens=150,  # Set the maximum number of tokens for the response
    )

# Get the response
answer = response.choices[0].text.strip()

# Display the response
print("Question:", prompt)
print("Answer:", answer)
