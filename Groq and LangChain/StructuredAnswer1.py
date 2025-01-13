from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

load_dotenv()

def get_python_help(question: str):
    llm = ChatGroq(
        model="mixtral-8x7b-32768",
    )
    
    prompt = f"""Please explain {question} in a structured format. 
    Return the response in this exact JSON format:
    {{
        "topic": "specific Python topic",
        "level": "beginner/intermediate/advanced",
        "explanation": "detailed explanation",
        "code_example": "code example if applicable",
        "common_pitfalls": "common mistakes to avoid"
    }}"""
    
    response = llm.invoke(prompt)
    
    # Parse and format the response
    try:
        structured_answer = json.loads(response.content)
        
        # Format the output nicely
        formatted_output = f"""
╭──────────────────────────────────────────────╮
│ PYTHON CONCEPT EXPLANATION                   │
╰──────────────────────────────────────────────╯
📌 Topic: {structured_answer['topic']}
🎯 Level: {structured_answer['level']}

📝 Explanation:
{structured_answer['explanation']}

💻 Code Example:
{structured_answer['code_example']}

⚠️ Common Pitfalls:
{structured_answer['common_pitfalls']}
"""
        return formatted_output
    
    except json.JSONDecodeError:
        return "Error: Could not parse the response"

# Example usage
if __name__ == "__main__":
    questions = [
        "how to use Python list comprehension",
        "explain Python decorators"
    ]
    
    for question in questions:
        print("\nQuestion:", question)
        answer = get_python_help(question)
        print(answer)
