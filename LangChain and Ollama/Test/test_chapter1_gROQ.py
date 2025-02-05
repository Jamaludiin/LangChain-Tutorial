# from chapter1_Ollama import 
# pytest -v test_chapter1_gROQ.py

import os
import pytest
from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture
def groq_llm():
    """Fixture to initialize Groq model."""
    groq_api_key = os.getenv('GROQ_API_KEY')
    if not groq_api_key:
        pytest.fail("GROQ_API_KEY environment variable is not set")

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=32767,
        timeout=10,
        max_retries=2,
    )

@pytest.mark.parametrize("prompt", [
    "Write a poem about AI",
    "Explain the importance of deep learning",
    "Describe the future of artificial intelligence"
])
def test_groq_response(groq_llm, prompt):
    """Test Groq model response."""
    response = groq_llm.invoke(prompt)

    # Ensure response is valid
    assert response, "Response should not be None"
    # Ensures that the response is not None or an empty object.
    # If response is None or evaluates to False, the test fails with the message "Response should not be None"
    
    assert isinstance(response.content, str), "Response should be a string"
    # Checks that response.content is of type str.
    # If response.content is not a string (e.g., None, list, dict), the test fails.
   
    assert len(response.content.strip()) > 0, "Response should not be empty"
    # Removes leading and trailing spaces using .strip() and ensures that the remaining content has a length greater than 0.
    # This prevents cases where the response is just empty spaces.

    # Optional: Check if response contains expected words
    assert any(word in response.content.lower() for word in prompt.lower().split()), "Response should be relevant to the prompt"
    # Ensures that at least one word from the prompt exists in the response.
    # Converts both the response.content and prompt to lowercase to make the check case-insensitive.
    # Splits the prompt into words and checks if any of them appear in response.content.