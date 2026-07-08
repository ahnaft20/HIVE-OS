from datetime import datetime


class AgentStateEngine:

    def __init__(self):

        self.states = {}

    def update(
        self,
        agent,
        state,
        detail="",
    ):

        self.states[agent] = {

            "state": state,

            "detail": detail,

            "updated": datetime.now().strftime("%H:%M:%S"),

        }

    def get(self):

        return self.states