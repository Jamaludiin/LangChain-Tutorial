import os
import json
import asyncio
from dotenv import load_dotenv
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.output_parsers import BaseGenerationOutputParser
from typing import Any, List, Dict

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)


# Custom Output Parser
class JSONOutputParser(BaseGenerationOutputParser):
    """Parses JSON output from LLM responses."""

    def parse_result(self, result: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not result:
            return {"error": "No output received"}
        
        output_text = result[0].get("text", "")

        try:
            parsed_output = json.loads(output_text)
            return parsed_output
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON", "output": output_text}


async def main():
    print("\n=== abatch() - Run multiple prompts asynchronously ===")
    prompts = ["Tell me a joke", "Give me a fun fact"]
    responses = await llm.abatch(prompts)
    for response in responses:
        print(response)

    print("\n=== abatch_as_completed() - Process multiple prompts as they complete ===")
    async for response in llm.abatch_as_completed(["Translate 'hello' to French", "What is 2 + 2?"]):
        print(response)

    print("\n=== ainvoke() - Run a single prompt asynchronously ===")
    response = await llm.ainvoke("Who won the FIFA World Cup in 2018?")
    print(response)

    print("\n=== aparse_result() - Parse result asynchronously ===")
    parser = JSONOutputParser()
    llm_response = [{"text": '{"name": "Alice", "age": 25}'}]
    parsed = await parser.aparse_result(llm_response)
    print(parsed)

    print("\n=== astream() - Stream output asynchronously ===")
    async for chunk in llm.astream("Tell me a short story"):
        print(chunk, end="")

    print("\n=== astream_events() - Stream structured events ===")
    async for event in llm.astream_events("Describe the Eiffel Tower"):
        print(event)


# Run async functions
asyncio.run(main())

print("\n=== batch() - Run multiple prompts synchronously ===")
responses = llm.batch(["What is the capital of Japan?", "Who discovered gravity?"])
for response in responses:
    print(response)

print("\n=== batch_as_completed() - Process batch responses as they complete ===")
for response in llm.batch_as_completed(["What is 5+5?", "Capital of Germany?"]):
    print(response)

print("\n=== bind() - Bind parameters for future calls ===")
llm_custom = llm.bind(temperature=0.5)
response = llm_custom.invoke("What is AI?")
print(response)

print("\n=== configurable_alternatives() - Show alternative configurations ===")
print(llm.configurable_alternatives())

print("\n=== configurable_fields() - Show configurable fields ===")
print(llm.configurable_fields())

print("\n=== invoke() - Run a single prompt synchronously ===")
response = llm.invoke("What is the meaning of life?")
print(response)

print("\n=== parse_result() - Parse JSON response ===")
parser = JSONOutputParser()
llm_response = [{"text": '{"city": "London", "country": "UK"}'}]
parsed = parser.parse_result(llm_response)
print(parsed)

print("\n=== stream() - Stream response synchronously ===")
for chunk in llm.stream("Explain quantum computing in simple terms."):
    print(chunk, end="")

print("\n=== with_alisteners() - Add asynchronous listeners ===")
llm_with_listeners = llm.with_alisteners([lambda x: print("Received:", x)])
response = llm_with_listeners.invoke("Tell me a fun fact")
print(response)

print("\n=== with_config() - Attach a config ===")
llm_with_config = llm.with_config({"timeout": 20})
response = llm_with_config.invoke("Explain blockchain.")
print(response)

print("\n=== with_fallbacks() - Set fallback models ===")
fallback_llm = ChatGroq(model="mistral-7b")
llm_with_fallbacks = llm.with_fallbacks([fallback_llm])
response = llm_with_fallbacks.invoke("What is deep learning?")
print(response)

print("\n=== with_listeners() - Add event listeners ===")
def listener(event):
    print("Event:", event)

llm_with_listeners = llm.with_listeners([listener])
response = llm_with_listeners.invoke("Tell me about space exploration.")
print(response)

print("\n=== with_retry() - Retry on failure ===")
llm_with_retry = llm.with_retry(max_retries=5)
response = llm_with_retry.invoke("What is the weather today?")
print(response)

print("\n=== with_types() - Specify return types ===")
llm_with_types = llm.with_types(str)
response = llm_with_types.invoke("Who is Albert Einstein?")
print(response)
