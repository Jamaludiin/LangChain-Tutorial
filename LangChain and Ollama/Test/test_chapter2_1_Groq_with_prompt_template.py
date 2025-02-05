import os
import pytest
import time
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# pytest -v test_chapter2_1_Groq_with_prompt_template.py


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
        max_tokens=32767,
        timeout=10,
        max_retries=2,
    )

@pytest.fixture(scope="module")
def prompt_template():
    """Fixture to create the ChatPromptTemplate."""
    return ChatPromptTemplate.from_messages(
        [
            ("system", "Generate a list of 10 synonyms for the following word. Return the results as a comma-separated list."),
            ("human", "{input}")
        ]
    )

@pytest.mark.parametrize("input_word", [
    "happy",
    "sad",
    "fast",
    "intelligent",
    "strong"
])
def test_groq_execution_time(groq_llm, prompt_template, input_word):
    """Test execution time using the specified ChatPromptTemplate."""
    chain = prompt_template | groq_llm

    start_time = time.time()
    response = chain.invoke({"input": input_word})
    end_time = time.time()

    response_time = end_time - start_time

    print(f"\nPrompt Input: {input_word}\nExecution Time: {response_time:.2f} seconds\nResponse: {response.content}\n")

    assert response_time < 10, f"Response took too long: {response_time:.2f} seconds"
    assert isinstance(response.content, str), "Response should be a string"
    assert "," in response.content, "Response should be a comma-separated list"
