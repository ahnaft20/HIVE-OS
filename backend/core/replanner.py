import ollama


SYSTEM_PROMPT = """
You are HIVE OS Replanning Engine.

One or more agents have failed.

Your task:

- Analyze the failure.
- Decide a new strategy.
- Reassign work.
- Keep the project moving.

Output:

# Failure Analysis

# New Execution Plan

# Reason
"""


def run(

    user_prompt,

    execution_plan,

    failure,

):

    prompt = f"""

User Request

{user_prompt}

====================

Original Plan

{execution_plan}

====================

Failure

{failure}

"""

    response = ollama.chat(

        model="llama3.2:3b",

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },

            {
                "role": "user",
                "content": prompt,
            },

        ],

    )

    return response["message"]["content"]