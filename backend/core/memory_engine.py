import json
from pathlib import Path


MEMORY_ROOT = Path("memory/projects")


class MemoryEngine:

    def __init__(self):

        MEMORY_ROOT.mkdir(
            parents=True,
            exist_ok=True,
        )

    def save_project(

        self,

        project_name,

        data,

    ):

        filepath = MEMORY_ROOT / f"{project_name}.json"

        with open(
            filepath,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def load_project(

        self,

        project_name,

    ):

        filepath = MEMORY_ROOT / f"{project_name}.json"

        if not filepath.exists():

            return None

        with open(
            filepath,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    def all_projects(self):

        projects = []

        for file in MEMORY_ROOT.glob("*.json"):

            projects.append(
                file.stem,
            )

        return sorted(projects)