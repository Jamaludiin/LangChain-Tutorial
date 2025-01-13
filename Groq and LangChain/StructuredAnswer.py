from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import List, Dict
import json

load_dotenv()

# Define a simple structure for questions
class Question:
    def __init__(self, question: str, answer: str, topic: str, level: str):
        self.question = question
        self.answer = answer
        self.topic = topic
        self.level = level
    
    def __str__(self):
        return f"""
                Topic: {self.topic}
                Level: {self.level}
                Q: {self.question}
                A: {self.answer}
                """

def get_structured_qa() -> List[Question]:
    llm = ChatGroq(
        model="mixtral-8x7b-32768",
    )
    
    # Prompt that asks for structured output
    prompt = """Generate 3 questions and answers about Artificial Intelligence. 
    Return them in the following JSON format:
    {
        "questions": [
            {
                "question": "question text here",
                "answer": "answer text here",
                "topic": "specific AI topic",
                "level": "beginner/intermediate/advanced"
            }
        ]
    }"""
    
    response = llm.invoke(prompt)
    
    # Parse the JSON response
    try:
        qa_data = json.loads(response.content)
        questions = []
        
        for q in qa_data['questions']:
            question = Question(
                question=q['question'],
                answer=q['answer'],
                topic=q['topic'],
                level=q['level']
            )
            questions.append(question)
            
        return questions
    
    except json.JSONDecodeError:
        print("Error: Could not parse JSON response")
        return []

# Example usage
if __name__ == "__main__":
    questions = get_structured_qa()
    
    # Access questions individually
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}:")
        print(q)
        
    # Access specific fields
    if questions:
        print("\nAccessing specific fields of first question:")
        first_q = questions[0]
        print(f"Question: {first_q.question}")
        print(f"Answer: {first_q.answer}")
        print(f"Topic: {first_q.topic}")
        print(f"Level: {first_q.level}")
