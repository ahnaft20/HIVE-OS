from core.fireworks_client import ask_llm


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

    return ask_llm(
        SYSTEM_PROMPT,
        prompt,
    )