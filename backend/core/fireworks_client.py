from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("FIREWORKS_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "FIREWORKS_API_KEY not found. Check backend/.env"
    )

MODEL = "accounts/fireworks/models/deepseek-v4-flash"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.fireworks.ai/inference/v1",
    timeout=120,
)

print("=" * 60)
print("🔥 FIREWORKS CLIENT INITIALIZED")
print("Model :", MODEL)
print("Base URL : https://api.fireworks.ai/inference/v1")
print("=" * 60)


def ask_llm(system_prompt: str, user_prompt: str):
    try:

        print("-" * 60)
        print("Sending request to Fireworks...")
        print("Model:", MODEL)
        print("-" * 60)

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

        print("✅ Fireworks response received.")

        return response.choices[0].message.content

    except Exception as e:
        print("=" * 60)
        print("❌ FIREWORKS ERROR")
        print(type(e).__name__)
        print(repr(e))
        print("=" * 60)
        raise