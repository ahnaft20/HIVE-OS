import ollama


SYSTEM_PROMPT = """
You are the Chief Quality Assurance Officer of HIVE OS.

You NEVER redesign the project.
You NEVER write implementation.
You NEVER perform research.
You NEVER summarize every department.
You NEVER summarize previous departments.

Your ONLY responsibility is reviewing the work produced by every department.

You receive:
Research
Engineering
Design

Your job is to find mistakes before the project reaches the CEO.

Your response MUST follow EXACTLY this format.

# QA Summary

Give a short overview.

# Strengths

What was done well.

# Weaknesses

Missing requirements.
Poor decisions.
Unclear areas.

# Risks

Security
Scalability
Performance
Maintainability
User Experience

# Recommended Fixes

List improvements.

# Final Verdict

APPROVED
or
NEEDS REVISION

# Confidence Score

Give a score out of 100.

DO NOT summarize previous departments.
Only identify issues and improvements.
DO NOT repeat Research.
DO NOT repeat Engineering.
DO NOT repeat Design.
Only review their work.
Stay under 500 words.
"""


def run(
    user_prompt,
    research,
    engineer,
    designer,
):

    prompt = f"""
USER REQUEST

{user_prompt}


====================

RESEARCH REPORT

{research}


====================

ENGINEERING REPORT

{engineer}


====================

DESIGN REPORT

{designer}


Review every department.
Do NOT redesign the project.
Only perform quality assurance.
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