
# pytest -v test_token_limit_testing.py


import os
import pytest
import time
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture(scope="module")
def groq_llm():
    """Fixture to initialize Groq model and validate API key."""
    groq_api_key = os.getenv('GROQ_API_KEY')
    if not groq_api_key:
        pytest.fail("GROQ_API_KEY environment variable is not set")
    
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=500,  # Set a reasonable token limit for testing
        timeout=10,
        max_retries=2,
    )


@pytest.mark.parametrize("prompt, expected_format", [
    ("Write a poem about AI", "string"),  # General test
    ("Give me 10 synonyms for 'happy'", "comma-separated"),  # Specific format test
    ("", "empty"),  # Edge case: Empty input
    ("12345", "number"),  # Edge case: Numeric input
    ("@#$%^&*()!", "symbols"),  # Edge case: Special characters
])
def test_groq_response(groq_llm, prompt, expected_format):
    """Test Groq model response for different prompts."""
    response = groq_llm.invoke(prompt)

    

    assert response, f"Response should not be None for prompt: {prompt}"
    assert isinstance(response.content, str), f"Response should be a string, got {type(response.content)}"
    assert len(response.content.strip()) > 0, f"Response should not be empty for prompt: {prompt}"

    # Ensure relevance: At least one word from prompt should appear in response
    assert any(word in response.content.lower() for word in prompt.lower().split()), \
        f"Response should be relevant to the prompt. Received: {response.content}"

    # Check format-specific expectations. BUT I DID NOT PROVIDED SUCH GUIDE TO THE LLM SO LLM MAY OR MAY NOT GIVE BECOZ HE HAS NO IDEA THE EXPECTED OUTPUT
    if expected_format == "comma-separated":
        assert "," in response.content, f"Expected comma-separated response, got: {response.content}"
    elif expected_format == "empty":
        assert response.content.strip() == "", f"Expected empty response, got: {response.content}"
    elif expected_format == "number":
        assert any(char.isdigit() for char in response.content), f"Expected numeric content, got: {response.content}"
    elif expected_format == "symbols":
        assert any(char in "@#$%^&*()!" for char in response.content), f"Expected special characters, got: {response.content}"

    # Ensure response token length is within the expected limit
    token_count = len(response.content.split())
    assert token_count <= 500, f"Response exceeded token limit. Got {token_count} tokens."


@pytest.mark.parametrize("prompt, token_limit", [
    ("Explain quantum computing in detail", 100),
    ("Give me a list of 50 adjectives", 200),
    ("Summarize the history of AI", 150)
])
def test_groq_token_limit(groq_llm, prompt, token_limit):
    """Test whether responses stay within the expected token limits."""
    response = groq_llm.invoke(prompt)

    assert response, f"Response should not be None for prompt: {prompt}"
    token_count = len(response.content.split())
    
    assert token_count <= token_limit, f"Expected at most {token_limit} tokens, but got {token_count}. This is the content: {response.content}"


