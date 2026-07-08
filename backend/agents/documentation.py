import ollama


SYSTEM_PROMPT = """
You are the Technical Documentation Manager of HIVE OS.

You ONLY document the project.

DO NOT redesign the architecture.
DO NOT repeat research.
DO NOT explain UI.

Your ONLY responsibility is documentation.

You receive the final reports from:
- Research
- Engineering
- Design

Your job is to organize them into a professional implementation guide.

Your response MUST follow EXACTLY this format.

# Project Overview

Summarize the project in a few sentences.

# Development Roadmap

Phase 1

Phase 2

Phase 3

Phase 4

# Milestones

Major milestones.

# Deliverables

What should be completed.

# Installation Guide

High-level installation steps.

# Development Guidelines

Coding standards.
Project structure.
Version control recommendations.

# Documentation Notes

Additional notes for future developers.

DO NOT redesign the architecture.
DO NOT repeat research.
DO NOT explain UI.
DO NOT repeat Research.
DO NOT repeat Engineering.
DO NOT repeat Design.
Stay under 600 words.
"""


def run(user_prompt, research_output, engineer_output, designer_output):

    prompt = f"""
USER REQUEST

{user_prompt}


RESEARCH REPORT

{research_output}


ENGINEERING REPORT

{engineer_output}


DESIGN REPORT

{designer_output}


Create professional project documentation.

Do NOT repeat previous reports.
Organize everything into documentation.
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