import os
import pytest
import time
from langchain_groq import ChatGroq
from dotenv import load_dotenv
# pytest -v test_execution_time.py

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

@pytest.mark.parametrize("prompt", [
    "Generate a detailed business proposal",
    "Explain the theory of relativity",
    "Summarize a 300-page book"
])
def test_groq_execution_time(groq_llm, prompt):
    """Test that response times are reasonable."""
    start_time = time.time()
    response = groq_llm.invoke(prompt)
    end_time = time.time()

    response_time = end_time - start_time

    print(f"\nPrompt: {prompt}\nExecution Time: {response_time:.2f} seconds\n")
    
    assert response_time < 10, f"Response took too long: {response_time:.2f} seconds"



# more test cases

@pytest.mark.parametrize("prompt, expected_format", [
    ("Write a poem about AI", "string"),  # General test
    ("Give me 10 synonyms for 'happy'", "comma-separated"),  # Specific format test
    ("", "empty"),  # Edge case: Empty input
    ("12345", "number"),  # Edge case: Numeric input
    ("@#$%^&*()!", "symbols"),  # Edge case: Special characters
])
def test_groq_response(groq_llm, prompt, expected_format):
    """Test Groq model response for different prompts."""
    start_time = time.time()  # Start timing the request
    response = groq_llm.invoke(prompt)
    end_time = time.time()  # End timing

    response_time = end_time - start_time

    assert response, f"Response should not be None for prompt: {prompt}"
    assert isinstance(response.content, str), f"Response should be a string, got {type(response.content)}"
    assert len(response.content.strip()) > 0, f"Response should not be empty for prompt: {prompt}"

    # Ensure relevance: At least one word from prompt should appear in response
    assert any(word in response.content.lower() for word in prompt.lower().split()), \
        f"Response should be relevant to the prompt. Received: {response.content}"

    # Check format-specific expectations
    if expected_format == "comma-separated":
        assert "," in response.content, f"Expected comma-separated response, got: {response.content}"
    elif expected_format == "empty":
        assert response.content.strip() == "", f"Expected empty response, got: {response.content}"
    elif expected_format == "number":
        assert any(char.isdigit() for char in response.content), f"Expected numeric content, got: {response.content}"
    elif expected_format == "symbols":
        assert any(char in "@#$%^&*()!" for char in response.content), f"Expected special characters, got: {response.content}"

    # Ensure execution time is reasonable
    assert response_time < 5, f"Response took too long: {response_time:.2f} seconds"

   


@pytest.mark.parametrize("prompt", [
    "Generate a detailed business proposal",
    "Explain the theory of relativity",
    "Summarize a 300-page book"
])
def test_groq_execution_time2(groq_llm, prompt):
    """Test that response times are reasonable."""
    start_time = time.time()
    response = groq_llm.invoke(prompt)
    end_time = time.time()

    response_time = end_time - start_time
    assert response_time < 10, f"Response took too long: {response_time:.2f} seconds"
