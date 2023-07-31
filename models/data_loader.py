import os
import yaml
import sys

from dataclasses import dataclass, field
from typing import List

@dataclass
class DataLoader:
    paths: dict
    adventure: any = field(default_factory=dict)

    def __init__(self, paths: dict):
        # If there's no 'adventures_path' key in the paths dict, throw an error
        if 'adventures_path' not in paths:
            raise ValueError("No 'adventures_path' key in paths dict")
        
        # If there's no 'characters_path' key in the paths dict, throw an error
        if 'characters_path' not in paths:
            raise ValueError("No 'characters_path' key in paths dict")
        
        self.paths = paths

    def load_adventure(self) -> dict:
        if len(sys.argv) < 2:
            print("Please specify an adventure name")
            sys.exit()

        adventure_name = sys.argv[1]

        if not os.path.exists(self.paths["adventures_path"] + adventure_name):
            print("Adventure " + adventure_name + " does not exist")
            sys.exit()

        self.adventure_path = self.paths["adventures_path"] + adventure_name + "/"
        self.characters_path = self.adventure_path + self.paths["characters_path"]

        # Load adventure information
        with open(self.adventure_path + "adventure.yaml", 'r') as stream:
            try:
                adventure = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        
        # Load characters
        adventure["characters"] = self.load_characters(adventure_name)

        self.adventure = adventure

        return self.adventure
    
    # Load a single character from a YAML file
    def load_character(self, character_file: str) -> dict:
        character = None

        with open(self.characters_path + character_file, 'r') as stream:
            try:
                character = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return character

    
    def load_characters(self, adventure_name: str) -> List[dict]:
        characters = []

        for character_file in os.listdir(self.characters_path):
            if character_file.endswith(".yaml"):
                character = self.load_character(character_file)
                characters.append(character)

        return characters