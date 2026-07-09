from core.fireworks_client import ask_llm

SYSTEM_PROMPT = """
You are the Internal Debate Engine of HIVE OS.

Your job is to review the work of multiple AI agents.

Find:

- Conflicting ideas
- Weak arguments
- Missing information
- Better alternatives

Do NOT choose a winner.

Return:

# Agreements

# Disagreements

# Suggestions

Keep the response concise and professional.
"""


def run(research, engineer, designer):

    prompt = f"""
Research Agent

{research}

====================

Engineer Agent

{engineer}

====================

Designer Agent

{designer}

Analyze every department.

Find disagreements.

Suggest improvements.
"""

    return ask_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=prompt,
    )