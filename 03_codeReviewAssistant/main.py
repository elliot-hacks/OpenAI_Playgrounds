import os
from openai import OpenAI



client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


file = open("code_test.py", "r").read()

messages = [{"role": "system", "content": "You are a sweet helpul, old grandma named Phoebe, born in 1954."}]

while True:
    user_input = input("What can Granny help you with: ")
    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
                          model="gpt-3.5-turbo",
                          messages=messages,
                          temperature=0.5,
                          max_tokens=1024,
                          )
    
    granny_ans = completion.choices[0].message.content
    print(f"\nGranny: {granny_ans}\n")
