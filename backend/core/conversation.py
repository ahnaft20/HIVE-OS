from datetime import datetime


class ConversationBoard:

    def __init__(self):

        self.messages = []

    def send(
        self,
        sender,
        receiver,
        message,
    ):

        self.messages.append(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "from": sender,
                "to": receiver,
                "message": message,
            }
        )

    def history(self):

        return self.messages