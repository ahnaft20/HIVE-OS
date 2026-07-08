class ModelRouter:

    def __init__(self):

        self.models = {

            "research": "llama3.2:3b",

            "backend": "deepseek-coder:6.7b",

            "frontend": "deepseek-coder:6.7b",

            "database": "deepseek-coder:6.7b",

            "devops": "deepseek-coder:6.7b",

            "security": "deepseek-coder:6.7b",

            "designer": "llama3.2:3b",

            "documentation": "llama3.2:3b",

            "qa": "llama3.2:3b",

            "product": "llama3.2:3b",

            "leader": "llama3.2:3b",

        }

    def choose(

        self,

        agent,

        prompt,

    ):

        return self.models

    def export(self):

        return self.models