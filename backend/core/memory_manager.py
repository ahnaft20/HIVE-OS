from core.memory_engine import MemoryEngine
from core.memory_search import MemorySearch


class MemoryManager:

    def __init__(self):

        self.engine = MemoryEngine()

        self.searcher = MemorySearch()

    def find(

        self,

        prompt,

    ):

        return self.searcher.search(
            prompt,
        )

    def save(

        self,

        project,

        data,

    ):

        self.engine.save_project(
            project,
            data,
        )

    def load(

        self,

        project,

    ):

        return self.engine.load_project(
            project,
        )

    def projects(self):

        return self.engine.all_projects()