import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1",
)

MODEL = "accounts/fireworks/models/deepseek-v3"


def ask_llm(system_prompt: str, user_prompt: str):

    response = client.chat.completions.create(

        model=MODEL,

        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],

        temperature=0.7,
        max_tokens=1500,

    )

    return response.choices[0].message.content