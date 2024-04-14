import os
import json
from openai import OpenAI



client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


def get_current_weather(location, unit="celcius"):
    """Get current weather in a given location."""
    weather_info = {
        "loaction": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["Sunny", "Windy"]
    }
    return json.dumps(weather_info)


def run():
    functions = [
        {
            "name": "get_current_weather",
            "description": "Get the current weather",

            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g Arusha, TZ",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celcius", "farhenheit"],
                    },
                },
                "required": ["location"],
            },
        }
    ]


    messages = [{"role": "user", "content": "What is the weather like in Mbeya"}]
    completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo-0613",
        functions=functions,
        function_call="auto",
    )

    print(completion)
    print()

    response=completion.choices[0].message
    # response=completion["choices"][0]["message"]

    if response.get("function_call"):
        availabe_functions = {
            "get_current_weather": get_current_weather,
        }

        function_name = response["function_call"]["name"]
        function_args = json.loads(response["function_call"]["arguments"])
        function_to_call = availabe_functions[function_name]
        function_return_value = function_to_call(
            location=function_args.get("location"),
            unit = function_args.get("unit"),
        )


        messages.append(response)

        messages.append(
            {
                "role": "function_return_value",
                "name": function_return_value,
                "content": function_return_value,
            }
        )


        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )

        print(second_response)
        print()
        print(second_response.choices[0].message.content)


if __name__ == "__main__":
    run()

