class Workspace:

    def __init__(self):

        self.data = {}

        self.messages = []

    def save(self, agent, output):

        self.data[agent] = output

    def read(self, agent):

        return self.data.get(agent, "")

    def notify(self, sender, receiver, message):

        self.messages.append({

            "from": sender,

            "to": receiver,

            "message": message,

        })

    def inbox(self, receiver):

        return [

            m

            for m in self.messages

            if m["to"] == receiver

        ]

    def all_messages(self):

        return self.messages