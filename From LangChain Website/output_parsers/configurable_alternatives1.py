"""
📌 Why Use configurable_alternatives()?
✔️ Dynamically switch configurations without reloading models.
✔️ Test different AI behaviors (e.g., conservative vs. creative responses).
✔️ Optimize responses based on user needs (e.g., serious vs. fun tone).

This method is useful when you need different AI behaviors on demand!
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema.runnable.configurable import ConfigurableField

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=100,
    timeout=10,
    max_retries=2,
)

# Define the configurable field (which setting we want to change dynamically)
temperature_field = ConfigurableField(id="temperature")

# Define alternative configurations
llm_with_alternatives = llm.configurable_alternatives(
    which=temperature_field,
    low=lambda: llm.with_config({"temperature": 0.2}),
    medium=lambda: llm.with_config({"temperature": 0.7}),
    high=lambda: llm.with_config({"temperature": 1.0}),
)

# Use different configurations dynamically
for key in ["low", "medium", "high"]:
    alternative_model = llm_with_alternatives.with_config({"temperature": key})
    response = alternative_model.invoke("Tell me a creative idea for a startup.")

    print(f"\n=== Config: {key} ===")
    print(response)
