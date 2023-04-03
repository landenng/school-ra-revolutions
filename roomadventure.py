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

class Game(Frame):
    
    EXIT_ACTIONS = ["quit", "exit", "bye", "q"]

    # status
    STATUS_DEFAULT = "I don't understand. Try <verb> <noun>. Valid verbs are go, look, and take."
    STATUS_DEAD = "You are dead."
    STATUS_BAD_EXIT = "Invalid exit."
    STATUS_ROOM_CHANGING = "Room changed."
    STATUS_GRABBED = "Item grabbed."
    STATUS_BAD_GRABBABLE = "I can't grab that."
    STATUS_BAD_ITEM = "I don't see that."
    
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, parent) -> None:
        self.inventory = []
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)

    def setup_game(self):
        # create rooms
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")

        # add exits to each room
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)

        r2.add_exit("west", r1)
        r2.add_exit("south", r4)

        r3.add_exit("north", r1)
        r3.add_exit("east", r4)

        r4.add_exit("north", r2)
        r4.add_exit("west", r3)
        r4.add_exit("south", None)

        # add items to the rooms
        r1.add_item("chair", "Something about wicker and legs")
        r1.add_item("bigger_chair", "More wicker and more legs")

        r2.add_item("fireplace", "hot. grab some fire and bring it.")
        r2.add_exit("more_chair", "even more wicker")

        r3.add_item("desk", "it is made of wicker also. a wicker desk.")
        r3.add_item("dimsdale_dimmadome", "owned by doug dimmadome, \
                    owner of the dimsdale dimmadome")
        r3.add_item("chair","another chair")

        r4.add_item("croissant", "it is made of butter. no dough.")

        # add grabbables to the rooms

        # set the current room to the starting room

    def setup_gui(self):
        pass

    def set_room_image(self):
        pass

    def set_status(self):
        pass

    def clear_entry(self):
        pass

    def handle_go(self):
        pass

    def handle_look(self):
        pass

    def handle_take(self):
        pass

    def play(self):
        pass

    def process(self, event):
        pass

