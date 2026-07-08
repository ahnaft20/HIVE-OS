import json
import os
from datetime import datetime


MEMORY_DIR = "memory"


if not os.path.exists(MEMORY_DIR):
    os.makedirs(MEMORY_DIR)


def save_project(
    project_name,
    data,
):

    file_path = os.path.join(
        MEMORY_DIR,
        f"{project_name}.json",
    )

    history = []

    if os.path.exists(file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as f:

            history = json.load(f)

    history.append({

        "timestamp": datetime.now().isoformat(),

        "conversation": data,

    })

    with open(
        file_path,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            history,
            f,
            indent=4,
            ensure_ascii=False,
        )


def load_project(project_name):

    file_path = os.path.join(
        MEMORY_DIR,
        f"{project_name}.json",
    )

    if not os.path.exists(file_path):
        return []

    with open(
        file_path,
        "r",
        encoding="utf-8",
    ) as f:

        return json.load(f)