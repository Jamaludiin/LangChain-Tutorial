from groq import Groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

load_dotenv()

class Calculator:
    def __init__(self):
        self.llm = ChatGroq(
            model="mixtral-8x7b-32768",
        )
    
    def calculate(self, num1: float, num2: float, operation: str) -> dict:
        prompt = f"""Perform {operation} on {num1} and {num2}.
        Return the response in this exact JSON format:
        {{
            "operation": "type of operation",
            "num1": first number,
            "num2": second number,
            "result": calculated result,
            "explanation": "step by step explanation"
        }}"""
        
        response = self.llm.invoke(prompt)
        return json.loads(response.content)

def display_calculation(calc_data: dict):
    print(f"""
╭──────────────────────────────────────────╮
│ CALCULATION RESULT                       │
╰──────────────────────────────────────────╯
📊 Operation: {calc_data['operation']}
🔢 Numbers: {calc_data['num1']} and {calc_data['num2']}
📝 Result: {calc_data['result']}
📌 Explanation: {calc_data['explanation']}
""")

def main():
    calc = Calculator()
    
    while True:
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            operations = {
                '1': 'addition',
                '2': 'subtraction',
                '3': 'multiplication',
                '4': 'division'
            }
            
            if choice in operations:
                result = calc.calculate(num1, num2, operations[choice])
                display_calculation(result)
            else:
                print("Invalid choice! Please try again.")
                
        except ValueError:
            print("Please enter valid numbers!")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 