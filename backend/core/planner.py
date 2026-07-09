from core.fireworks_client import ask_llm

SYSTEM_PROMPT = """
You are the Planning Engine of HIVE OS.

Choose which specialist experts are required.

Available experts

research

backend

frontend

database

devops

security

designer

documentation

qa

product

Return ONLY valid JSON.

Example

{
"research":true,
"backend":true,
"frontend":true,
"database":false,
"devops":false,
"security":true,
"designer":true,
"documentation":true,
"qa":true,
"product":true
}
"""


def create_plan(user_prompt, previous_context=None):

    if previous_context is None:
        previous_context = []

    # Build context string for previous projects
    previous_context_text = ""
    if previous_context:
        previous_context_text = f"""
========================
PREVIOUS PROJECT MEMORY
{previous_context}
========================
"""

    return ask_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
    )