# error 
# Groq is enough for generating responses, but in your case, the issue is related to token counting and message trimming in LangChain, which relies on a tokenizer.


"""
Groq is enough for generating responses, but LangChain needs a tokenizer for trimming messages. You can fix this by:
    Using an open-source tokenizer (Mistral-7B, LLaMA 3) from Hugging Face.
    Using an approximate token counter if you don’t want to install anything extra.
"""

"""
Groq is enough for generating responses, but in your case, the issue is related to token counting and message trimming in LangChain, which relies on a tokenizer.

Here's why Groq alone isn't handling it:

1. LangChain Needs a Token Counter for trim_messages()
    When using trim_messages(), LangChain needs to count tokens to ensure the message history doesn't exceed the limit.
    The default token counter uses OpenAI’s tokenizer (tiktoken), which doesn’t support Groq models like LLaMA 3 directly.
    Since you're switching from OpenAI to Groq, you need a compatible token counter.
2. Hugging Face is Required for Tokenization
    Since Groq doesn’t provide its own tokenizer in LangChain, Hugging Face is used for tokenizing Groq-compatible models like LLaMA 3.
    You're getting an error because Hugging Face is trying to load meta-llama/Llama-2-7b-chat-hf, which is gated.
    This means you need to either log in or use a different open-source tokenizer.

How to Fix It Without OpenAI
    You have two options:

    ✅ Option 1: Use a Compatible Hugging Face Tokenizer

    ✅ Option 2: Approximate Token Count
        If you don’t want to install Hugging Face, use a simple word counter:
"""
import os
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    trim_messages,
)
from langchain_groq import ChatGroq
from transformers import AutoTokenizer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)


# Load tokenizer for LLaMA models
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# Custom token counter function
def count_tokens(messages):
    text = " ".join(msg.content for msg in messages)
    return len(tokenizer.encode(text))

# Define a chat history
messages = [
    SystemMessage("You're a helpful assistant."),
    HumanMessage("What's the capital of France?"),
    AIMessage("The capital of France is Paris."),
    HumanMessage("Tell me a fun fact about it."),
    AIMessage("Paris is known as the 'City of Light' because it was one of the first cities to use streetlights."),
    HumanMessage("What are some famous landmarks in Paris?"),
]

# Trim the messages using the custom token counter
trimmed_messages = trim_messages(
    messages,
    strategy="last",
    token_counter=count_tokens,  # Use the custom token counter
    max_tokens=30,
    start_on="human",
    end_on=("human", "tool"),
    include_system=True
)

# Print the trimmed messages
for msg in trimmed_messages:
    print(f"{msg.__class__.__name__}: {msg.content}")
