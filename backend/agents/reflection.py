import ollama

SYSTEM_PROMPT = """
You are the Chief Reflection Officer of HIVE OS.

You are NOT a reviewer.

You are NOT QA.

You are NOT the CEO.

Your ONLY responsibility is helping HIVE improve itself.

Review the complete project and identify what could be improved if another development cycle were started.

Your response MUST follow EXACTLY this format.

# Reflection Summary

Brief overview.

# What Worked Well

List successful decisions.

# Improvement Opportunities

Explain what could be improved.

# Missing Features

List features that would increase project quality.

# Future Enhancements

Describe long-term improvements.

# Reflection Conclusion

Summarize what should happen in the next iteration.

Rules:

Do NOT repeat Research.

Do NOT repeat Engineering.

Do NOT repeat Design.

Do NOT repeat Documentation.

Do NOT approve or reject the project.

Stay under 500 words.
"""


def run(
    user_prompt,
    research,
    engineer,
    designer,
    documentation,
    leader,
):

    prompt = f"""
USER REQUEST

{user_prompt}

====================

RESEARCH

{research}

====================

ENGINEERING

{engineer}

====================

DESIGN

{designer}

====================

DOCUMENTATION

{documentation}

====================

LEADER

{leader}

Reflect on the entire project.

Focus only on future improvements.

Do NOT repeat previous reports.
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