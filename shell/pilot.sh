curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a programing and hacking assistant, skilled in explaining complex programming concepts with creative flair."
      },
      {
        "role": "user",
        "content": "write a python script for buffer overflow on eip with offset of 122 chars and return address 0xc0ded00d"
      }
    ]
  }'