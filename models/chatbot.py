import openai
import os

from dataclasses import dataclass

@dataclass
class Chatbot:
    model: str = "gpt-3.5-turbo-0613"
    temperature = 0.7
    max_tokens = 500

    openai_api_key = os.getenv('OPENAI_API_KEY')

    def get_completion(self, adventure_info: str, prompt: str) -> str:
        openai.api_key = os.getenv('OPENAI_API_KEY')

        system_instructions = "You are an assistant for a Game Master in a roleplaying game. Here's information about the game:\n\n"
        system_message = system_instructions + adventure_info

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]

        args = {
            'model': self.model,
            'messages': messages,
            'max_tokens': self.max_tokens,
            'temperature': self.temperature
        }

        completion = openai.ChatCompletion.create(**args)

        return completion
    