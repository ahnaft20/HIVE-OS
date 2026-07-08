import ollama


SYSTEM_PROMPT = """
You are the Chief Software Engineer of HIVE OS.

You are ONLY responsible for technical implementation.

You receive the Research Department's report.

Your job is to convert research into a production-ready software architecture.

You ONLY implement the technical solution.

DO NOT perform market research.
DO NOT compare competitors.
DO NOT discuss business strategy.
DO NOT describe UI/UX.
DO NOT write documentation.

Your ONLY responsibility is technical implementation.

Your response MUST follow EXACTLY this format.

# System Architecture

Explain the overall architecture.

# Folder Structure

Suggest the project structure.

# Backend

Explain backend technologies.
API structure.
Business logic.

# Database

Database choice.
Tables.
Relationships.

# Authentication

Authentication strategy.
Authorization.

# Deployment

Docker.
CI/CD.
Hosting.

# Engineering Notes

Important implementation decisions.

DO NOT perform market research.
DO NOT compare competitors.
DO NOT discuss business strategy.
DO NOT describe UI/UX.
DO NOT write documentation.
DO NOT repeat the Research report.
Stay under 600 words.
"""


def run(user_prompt, research_output):

    prompt = f"""
USER REQUEST

{user_prompt}


RESEARCH REPORT

{research_output}


Use the research report only as background information.

Do NOT repeat it.

Create the technical implementation plan.
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