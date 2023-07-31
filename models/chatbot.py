from dataclasses import dataclass, field

@dataclass
class Chatbot:
    def get_completion(self, adventure: dict, prompt: str) -> str:
        return "This is a test"
    