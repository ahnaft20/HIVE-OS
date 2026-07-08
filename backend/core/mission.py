import threading


class Mission:

    def __init__(self):

        self.lock = threading.Lock()

        self.name = ""

        self.progress = 0

        self.current = "Idle"

        self.completed = []

        self.remaining = []

        self.timeline = []

    def start(
        self,
        mission_name,
        stages,
    ):

        with self.lock:

            self.name = mission_name

            self.progress = 0

            self.current = stages[0]

            self.completed = []

            self.remaining = stages.copy()

            self.timeline = []

    def update(self, stage):

        with self.lock:

            self.current = stage

            if stage in self.remaining:

                self.remaining.remove(stage)

            if stage not in self.completed:

                self.completed.append(stage)

            total = (
                len(self.completed)
                + len(self.remaining)
            )

            if total == 0:

                self.progress = 100

            else:

                self.progress = int(
                    len(self.completed)
                    / total
                    * 100
                )

            self.timeline.append(
                {
                    "stage": stage,
                    "progress": self.progress,
                }
            )

    def finish(self):

        self.progress = 100

        self.current = "Completed"

    def export(self):

        return {

            "mission": self.name,

            "progress": self.progress,

            "current": self.current,

            "completed": self.completed,

            "remaining": self.remaining,

            "timeline": self.timeline,

        }