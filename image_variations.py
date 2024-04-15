import os
from openai import OpenAI

client = OpenAI()
OpenAI.api_key=os.getenv("OPENAI_API_KEY")


response = client.images.create_variation(
    model="dall-e-2",
    user="Painting of a billboard across the road.",
    image=open("./shelbyCountyAlabama.png", "rb"),
    n=2,
    size="1024x1024"
)

image_url = response.data[0].url
print(response)
print()
print(image_url)

