import ollama

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