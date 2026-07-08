import time

from agents.research import research_agent
from agents.engineer import engineer_agent
from agents.designer import designer_agent
from agents.leader import leader_agent


def run_hive(user_prompt):

    timeline = []

    # -------------------
    # Research
    # -------------------
    timeline.append({
        "agent": "Research",
        "status": "thinking"
    })

    research = research_agent(user_prompt)

    timeline[-1]["status"] = "done"
    timeline[-1]["output"] = research

    time.sleep(0.3)

    # -------------------
    # Engineer
    # -------------------
    timeline.append({
        "agent": "Engineer",
        "status": "thinking"
    })

    engineer = engineer_agent(
        user_prompt,
        research
    )

    timeline[-1]["status"] = "done"
    timeline[-1]["output"] = engineer

    time.sleep(0.3)

    # -------------------
    # Designer
    # -------------------
    timeline.append({
        "agent": "Designer",
        "status": "thinking"
    })

    designer = designer_agent(
        user_prompt,
        research,
        engineer
    )

    timeline[-1]["status"] = "done"
    timeline[-1]["output"] = designer

    time.sleep(0.3)

    # -------------------
    # Leader
    # -------------------
    timeline.append({
        "agent": "Leader",
        "status": "thinking"
    })

    leader = leader_agent(
        user_prompt,
        research,
        engineer,
        designer
    )

    timeline[-1]["status"] = "done"
    timeline[-1]["output"] = leader

    return {
        "timeline": timeline,
        "final": leader
    }