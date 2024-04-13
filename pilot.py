import os
from openai import OpenAI



client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a programing and hacking assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "write a python exploit to buffer overflow an eip with offset 123"}
  ],
  # temperature=0.5,
  # max_tokens=100,
)

msg=completion.choices[0].message
print(msg)