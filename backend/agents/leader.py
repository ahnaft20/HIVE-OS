import ollama


SYSTEM_PROMPT = """
You are the CEO of HIVE OS.

You are the CEO.

DO NOT summarize every department.
DO NOT repeat Research.
DO NOT repeat Engineering.
DO NOT repeat Design.

Your job is ONLY to make executive decisions.

For every department:

Approve
Reject
Modify
Explain WHY.

Then produce one final company decision.

Do NOT mention Reflection, Peer Review or Replanner if they were not executed.

Your job is NOT to summarize.

Your job is to LEAD.

Follow this exact decision process:

STEP 1

Review the Research report.

Decide whether the business analysis is sufficient.

STEP 2

Review Engineering.

Verify whether the implementation satisfies the Research team's recommendations.

STEP 3

Review Design.

Verify whether the UI supports the engineering plan.

STEP 4

Review all available internal analyses before making your executive decision.

Do not explicitly reference Reflection, Peer Review or Replanner unless their reports are presented to the user.

Produce one unified executive decision.

STEP 5

Make the FINAL COMPANY DECISION.

You MUST:

• Reject weak ideas.
• Resolve disagreements.
• Approve the strongest solution.
• Explain WHY you made every important decision.

Never summarize reports.
Never copy department outputs.
Think like the CEO of a software company.
"""


def run(
    user_prompt,
    research_output,
    engineer_output,
    designer_output,
    previous_context=None,
    reflection="",
    peer_review="",
    replan="",
):

    if previous_context is None:
        previous_context = []

    memory_text = (
        "\n".join(str(item) for item in previous_context)
        if previous_context
        else "No previous project memory available."
    )

    prompt = f"""
USER REQUEST

{user_prompt}


====================

PREVIOUS MEMORY

{memory_text}


====================

RESEARCH REPORT

{research_output}


====================

ENGINEERING REPORT

{engineer_output}


====================

DESIGN REPORT

{designer_output}


====================

PEER REVIEW

{peer_review}


====================

REFLECTION

{reflection}


====================

REPLANNING

{replan}


Act as the CEO of HIVE OS.

Your job is NOT to summarize.

Your job is to LEAD.

Follow this exact decision process:

STEP 1

Review the Research report.

Decide whether the business analysis is sufficient.

STEP 2

Review Engineering.

Verify whether the implementation satisfies the Research team's recommendations.

STEP 3

Review Design.

Verify whether the UI supports the engineering plan.

STEP 4

Review all available internal analyses before making your executive decision.

Do not explicitly reference Reflection, Peer Review or Replanner unless their reports are presented to the user.

Produce one unified executive decision.

STEP 5

Make the FINAL COMPANY DECISION.

You MUST:

• Reject weak ideas.
• Resolve disagreements.
• Approve the strongest solution.
• Explain WHY you made every important decision.

Never summarize reports.
Never copy department outputs.
Think like the CEO of a software company.
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