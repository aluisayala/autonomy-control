class FactCheckAPIClient:
    def check(self, statement):
        return True

class OpenAIConfidenceClient:
    def get_confidence(self, prompt):
        return 0.9