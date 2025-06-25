class KnowledgeBase:
    def __init__(self):
        self.memory = {}

    def recall(self, key):
        return self.memory.get(key, None)

    def store(self, key, value):
        self.memory[key] = value