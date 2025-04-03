"""
12. parse_result() - Parse LLM Output into Structured Data
This method converts raw LLM output into structured format (like JSON).
"""

import json
from langchain_core.output_parsers import BaseGenerationOutputParser

class JSONOutputParser(BaseGenerationOutputParser):
    """Parses JSON output from LLM responses."""
    
    def parse_result(self, result):
        try:
            return json.loads(result[0]["text"])
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON"}

parser = JSONOutputParser()
response = [{"text": '{"name": "Alice", "age": 25}'}]
parsed = parser.parse_result(response)

print("\n=== parse_result() Output ===")
print(parsed)
