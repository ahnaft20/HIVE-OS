from datetime import datetime


class AgentFactory:

    def __init__(self):

        self.agents = {}

    def create(
        self,
        name,
        role,
        team="Core",
    ):

        self.agents[name] = {

            "name": name,

            "role": role,

            "team": team,

            "status": "Idle",

            "created": datetime.now().strftime("%H:%M:%S"),

        }

    def update_status(
        self,
        name,
        status,
    ):

        if name in self.agents:

            self.agents[name]["status"] = status

    def team(self, name):

        if name not in self.agents:

            return None

        return self.agents[name]["team"]

    def remove(self, name):

        if name in self.agents:

            del self.agents[name]

    def get(self):

        return self.agents