import os
from openai import OpenAI



client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


file = open("code_test.py", "r").read()

messages = [{"role": "system", "content": "You are a code review assistant, to provide helpful code reviews in python"},]

while True:
    user_input = file
    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
                          model="gpt-3.5-turbo",
                          messages=messages,
                          temperature=0.5,
                          max_tokens=1024,
                          )
    
    code_review = completion.choices[0].message.content
    print(f"\nCode Review: {code_review}\n")
