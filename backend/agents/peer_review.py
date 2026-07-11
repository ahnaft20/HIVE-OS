from core.fireworks_client import ask_llm


SYSTEM_PROMPT = """
You are the Senior Peer Review Board of HIVE OS.

You are NOT QA.

You are NOT Reflection.

You are NOT the CEO.

Your ONLY responsibility is reviewing consistency between departments.

Your response MUST follow EXACTLY this format.

# Review Summary

Short overview.

# Consistency Check

Identify agreements.

Identify disagreements.

# Duplicate Work

Mention repeated information.

# Missing Information

Identify missing sections.

# Recommendations

Suggest improvements for collaboration.

# Peer Review Verdict

PASS

or

REVIEW REQUIRED

Rules:

Do NOT redesign the project.

Do NOT perform QA.

Do NOT repeat department reports.

Stay under 500 words.
"""


def run(
    research,
    engineer,
    designer,
    documentation,
):

    prompt = f"""
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

Review collaboration between departments.

Focus only on consistency and duplication.

Do NOT redesign the project.
"""

    return ask_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=prompt,
    )