from datetime import datetime
import threading


class StreamEngine:

    def __init__(self):

        self.lock = threading.Lock()

        self.logs = []

    def push(
        self,
        agent,
        message,
    ):

        with self.lock:

            self.logs.append(
                {
                    "time": datetime.now().strftime("%H:%M:%S"),
                    "agent": agent,
                    "message": message,
                }
            )

    def history(self):

        return self.logs