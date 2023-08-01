import os
import sys

from models.chatbot import Chatbot
from models.data_loader import DataLoader


def get_args():
    if len(sys.argv) < 2:
        print("Please specify an adventure name")
        sys.exit()

    adventure_name = sys.argv[1]
    adventure_path = adventures_path + adventure_name + "/"
        
    if not os.path.exists(adventure_path):
        print("Adventure " + adventure_name + " does not exist")
        sys.exit()

    return adventure_name, adventure_path


adventures_path = "adventures/"
adventure_name, adventure_path = get_args()
data_loader = DataLoader(adventure_name = adventure_name, adventure_path = adventure_path)
chatbot = Chatbot()

adventure_info: str = data_loader.load_adventure()
print(adventure_info)

# Main function
def main():

    # Loop, asking for input
    while True:
        prompt = input("Enter a prompt: ")
        if prompt == "exit":
            print("Exiting...")
            break

        response = chatbot.get_completion(adventure_info = adventure_info, prompt = prompt)
        print(response.choices[0].message.content)

        # TODO: Add a way to save the response to a file
        # TODO: Add chat history

# Run main function
if __name__ == "__main__":
    main()
