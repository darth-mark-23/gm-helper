import os
import sys

from models.chatbot import Chatbot
from models.data_loader import DataLoader

adventures_path = "adventures/"
characters_path = "characters/"

data_loader = DataLoader({
    "adventures_path": adventures_path,
    "characters_path": characters_path
})

chatbot = Chatbot()

# Main function
def main():
    adventure: dict = data_loader.load_adventure()
    print("Adventure name: " + adventure["name"])
    print(adventure)

    # Loop, asking for input
    while True:
        prompt = input("Enter a prompt: ")
        if prompt == "exit":
            print("Exiting...")
            break

        response = chatbot.get_completion(adventure = adventure, prompt = prompt)
        print(response)

# Run main function
if __name__ == "__main__":
    main()
