"""
4. aparse_result() - Parse JSON Response Asynchronously
This method parses structured JSON output from the model.
"""

import json
import asyncio
from langchain_core.output_parsers import BaseGenerationOutputParser
from langchain_groq import ChatGroq

class JSONOutputParser(BaseGenerationOutputParser):
    """Parses JSON output from LLM responses."""
    
    def parse_result(self, result):
        try:
            return json.loads(result[0]["text"])
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON"}

async def main():
    parser = JSONOutputParser()
    llm_response = [{"text": '{"name": "Alice", "age": 25}'}]
    parsed = await parser.aparse_result(llm_response)

    print("\n=== aparse_result() Output ===")
    print(parsed)

# Run the async function
asyncio.run(main())
