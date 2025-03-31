"""
Suppose we have an LLM that generates text, and we want to extract structured information from it. Let's implement a simple parser using BaseGenerationOutputParser.
"""

from langchain_core.output_parsers import BaseGenerationOutputParser
from typing import Any, List, Dict

class JSONOutputParser(BaseGenerationOutputParser):
    """Custom parser to extract JSON from LLM output."""

    def parse_result(self, result: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Parses the LLM output, assuming it generates a JSON-like response.
        """
        if not result:
            return {"error": "No output received"}
        
        # Assume the first result contains the main response
        output_text = result[0]['text']
        
        # Try to parse as JSON
        try:
            import json
            parsed_output = json.loads(output_text)
            return parsed_output
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON", "output": output_text}

# Example usage
parser = JSONOutputParser()
fake_llm_response = [{"text": '{"name": "Alice", "age": 25}'}]
parsed_data = parser.parse_result(fake_llm_response)

print(parsed_data)
