import threading
from datetime import datetime


class LiveWorkspace:

    def __init__(self):

        self.lock = threading.Lock()

        self.data = {
            "Leader": {
                "status": "Idle",
                "output": "",
                "updated": "",
            },
            "Research": {
                "status": "Idle",
                "output": "",
                "updated": "",
            },
            "Engineer": {
                "status": "Idle",
                "output": "",
                "updated": "",
            },
            "Designer": {
                "status": "Idle",
                "output": "",
                "updated": "",
            },
            "Documentation": {
                "status": "Idle",
                "output": "",
                "updated": "",
            },
            "QA": {
                "status": "Idle",
                "output": "",
                "updated": "",
            },
        }

        self.timeline = []

    def update(self, agent, status, output=""):

        with self.lock:

            self.data[agent]["status"] = status

            self.data[agent]["output"] = output

            self.data[agent]["updated"] = datetime.now().strftime("%H:%M:%S")

            self.timeline.append(
                {
                    "time": self.data[agent]["updated"],
                    "agent": agent,
                    "status": status,
                }
            )

    def get_workspace(self):

        return self.data

    def get_timeline(self):

        return self.timeline