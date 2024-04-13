import os
from openai import OpenAI



client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


user_input = input("What can Granny help you with: ")



completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a sweet helpul, old grandma named Phoebe, born in 1954."},
    {"role": "user", "content": user_input}
  ],
  temperature=0.5,
  max_tokens=1024,
)

msg=completion.choices[0].message.content
print(completion)
print(msg)
