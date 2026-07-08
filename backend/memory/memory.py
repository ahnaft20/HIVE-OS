# backend/memory/memory.py

class MemoryStore:
    def __init__(self):
        self.chat_history = []

    def add_user(self, message: str):
        self.chat_history.append({
            "role": "user",
            "content": message
        })

    def add_assistant(self, message: str):
        self.chat_history.append({
            "role": "assistant",
            "content": message
        })

    def get_history(self):
        return self.chat_history

    def clear(self):
        self.chat_history = []

    def trim(self, max_items: int = 12):
        if len(self.chat_history) > max_items:
            self.chat_history = self.chat_history[-max_items:]