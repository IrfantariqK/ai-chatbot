import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)

def start_chat():
    print("AI ChatBot: Hi there! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("AI ChatBot: Goodbye!")
            break
        response = generate_response(user_input)
        print(f"AI ChatBot: {response}")

if __name__ == "__main__":
    start_chat()
