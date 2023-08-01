import markdown
import os
import sys
import yaml

from dataclasses import dataclass
from typing import List

@dataclass
class DataLoader:
    adventure_name: str
    adventure_path: str
    adventure_info: str = ""

    def __init__(self, adventure_name: str, adventure_path: str):
        self.adventure_name = adventure_name
        self.adventure_path = adventure_path

    def load_adventure(self) -> str:
        # Load adventure information
        with open(self.adventure_path + "adventure.yaml", 'r') as stream:
            try:
                adventure_yaml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        
        # Get adventure topics
        if "topics" not in adventure_yaml:
            print("No topics found in adventure.yaml")
            sys.exit()
        topics = adventure_yaml["topics"]

        # Load topics
        self.adventure_info = self.load_topics(topics)

        return self.adventure_info
    
    def load_topics(self, adventure_name: str) -> List[dict]:
        # For each topic, load the topic markdown file and append it to the adventure info, separated by a newline
        for topic in adventure_name:
            topic_path = self.adventure_path + topic + ".md"
            # If the topic file exists, load it
            if os.path.exists(topic_path):
                with open(topic_path, 'r') as stream:
                    try:
                        markdown_text = stream.read()
                        # Process the markdown_text string here
                    except Exception as exc:
                        print(exc)
                
                # Append the markdown text to the adventure info
                self.adventure_info += markdown_text + "\n\n"
            else:
                print("Topic " + topic + " does not exist -- skipping...")

        return self.adventure_info