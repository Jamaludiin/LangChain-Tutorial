import os
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages.base import merge_content
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Groq API key from environment variables
groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the Groq chat model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=32767,
    timeout=10,
    max_retries=2,
)

# Example usage of merge_content

# Case 1: Merging string contents
content1 = "Hello"
content2 = "World!"
merged_strings = merge_content(content1, content2)
print("Merged Strings:", merged_strings)

# Case 2: Merging lists of strings
content_list1 = ["Hello", "this is"]
content_list2 = ["a merged", "message."]
merged_lists = merge_content(content_list1, content_list2)
print("Merged Lists:", merged_lists)

# Case 3: Merging dictionary-based content
content_dict1 = [{"type": "text", "value": "Hello"}]
content_dict2 = [{"type": "text", "value": "World!"}]
merged_dicts = merge_content(content_dict1, content_dict2)
print("Merged Dictionaries:", merged_dicts)

# Case 4: Mixing strings and lists
mixed_merge = merge_content(content1, content_list1)
print("Mixed Merge:", mixed_merge)
