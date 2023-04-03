# Name: Landen Nguyen
# Date: March 29, 2023
# Desc: Room Adventure Revolutions

from tkinter import *


class Room:
    """A Room has a name and a file path that points to a .gif image."""

    def __init__(self, name: str, image_filepath: str) -> None:
        self.name = name
        self.image = image_filepath
        self.exits = {}
        self.items = {}
        self.grabbables = []

    # skipping getters and setters
    def add_exit(self, label: str, room: "Room"):
        self.exits[label] = room

    def add_item(self, label: str, desc: str):
        self.items[label] = desc

    def add_grabbables(self, label: str):
        self.grabbables.append(label)

    def del_grabbables(self, label: str):
        self.grabbables.remove(label)

    def __str__(self) -> str:
        # create base response
        result = f"You are in {self.name}\n"

        # append the items you see in the room
        result += f"You see: "
        for item in self.items.keys():
            result += item + " "
        result += "\n"

        # append the exits available
        result += "Exits: "
        for exit in self.exits.keys():
            result += exit + " "
        result += "\n"

        return result

class Game:
    pass