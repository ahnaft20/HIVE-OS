import json
import os


GRAPH_FILE = "memory/knowledge_graph.json"


class KnowledgeGraph:

    def __init__(self):

        if os.path.exists(GRAPH_FILE):

            with open(
                GRAPH_FILE,
                "r",
                encoding="utf-8",
            ) as f:

                self.graph = json.load(f)

        else:

            self.graph = {
                "nodes": [],
                "edges": []
            }

    def add_node(self, node):

        if node not in self.graph["nodes"]:

            self.graph["nodes"].append(node)

    def add_edge(
        self,
        source,
        target,
        relation="related_to",
    ):

        edge = {
            "source": source,
            "target": target,
            "relation": relation,
        }

        if edge not in self.graph["edges"]:

            self.graph["edges"].append(edge)

    def save(self):

        with open(
            GRAPH_FILE,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                self.graph,
                f,
                indent=4,
                ensure_ascii=False,
            )

    def export(self):

        return self.graph