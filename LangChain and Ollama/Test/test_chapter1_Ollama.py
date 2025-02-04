# from chapter1_Ollama import 
# pytest -v test_chapter1_Ollama.py

import pytest
#from langchain.llms import Ollama
from langchain_community.llms import Ollama  # Updated import

@pytest.fixture
def ollama_llm():
    """Fixture to initialize Ollama model."""
    return Ollama(model="llama2")

@pytest.mark.parametrize("prompt", [
    "Write a poem about AI",
    "Explain the concept of machine learning",
    "Generate a short story about robots"
])
def test_ollama_response(ollama_llm, prompt):
    """Test Ollama model response."""
    response = ollama_llm.invoke(prompt)
    
    # Ensure the response is a non-empty string
    assert isinstance(response, str)
    assert len(response.strip()) > 0

    # Optional: Check for expected words in the response
    assert any(word in response.lower() for word in prompt.lower().split())
