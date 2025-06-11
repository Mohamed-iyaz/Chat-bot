import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [{"role": "system", "content": "You are a helpful assistant."}]

def chat_with_gpt(user_input):
    messages.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    reply = response.choices[0].message.content.strip()
    
    messages.append({"role": "assistant", "content": reply})
    
    return reply

if __name__ == "__main__":
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
