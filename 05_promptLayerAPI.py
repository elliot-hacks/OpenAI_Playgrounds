import os
import promptlayer


# Prompt layer tracks openai requests can be useful for billing of tokens 
promptlayer.api_key = os.getenv("PROMPTLAYER_API_KEY")
OpenAI = promptlayer.openai.OpenAI
client = OpenAI()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an assistant."},
    {"role": "user", "content": "Compose a poem please."}
  ],
  pl_tags=["getting-started"]
)


msg=completion.choices[0].message.content
print(msg)

