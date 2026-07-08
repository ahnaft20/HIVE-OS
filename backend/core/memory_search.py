from core.memory_engine import MemoryEngine


class MemorySearch:

    def __init__(self):

        self.memory = MemoryEngine()

    def search(

        self,

        user_prompt,

    ):

        prompt = user_prompt.lower()

        matches = []

        for project in self.memory.all_projects():

            if project.lower() in prompt:

                matches.append(project)

        return matches