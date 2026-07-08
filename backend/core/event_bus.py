class EventBus:

    def __init__(self):

        self.subscribers = {}

        self.event_log = []

    def subscribe(
        self,
        event_name,
        callback,
    ):

        self.subscribers.setdefault(
            event_name,
            [],
        ).append(callback)

    def publish(
        self,
        event_name,
        payload=None,
    ):

        self.event_log.append({

            "event": event_name,

            "payload": payload,

        })

        results = []

        for callback in self.subscribers.get(
            event_name,
            [],
        ):

            results.append(
                callback(payload)
            )

        return results

    def history(self):

        return self.event_log