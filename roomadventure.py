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
    STATUS_ROOM_CHANGE = "Room changed."
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
        r1 = Room("Room 1", "images/room1.gif")
        r2 = Room("Room 2", "images/room2.gif")
        r3 = Room("Room 3", "images/room3.gif")
        r4 = Room("Room 4", "images/room4.gif")

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
        r2.add_item("more_chair", "even more wicker")

        r3.add_item("desk", "it is made of wicker also. a wicker desk.")
        r3.add_item("dimsdale_dimmadome", "owned by doug dimmadome, \
                    owner of the dimsdale dimmadome")
        r3.add_item("chair","another chair")

        r4.add_item("croissant", "it is made of butter. no dough.")

        # add grabbables to the rooms

        r1.add_grabbables("key")

        r2.add_grabbables("fire")

        r3.add_grabbables("doug")

        r4.add_grabbables("butter")

        # set the current room to the starting room
        self.current_room = r1

    def setup_gui(self):
        # input element at the bottom of the screen
        self.player_input = Entry(self, bg='white', fg='black')
        self.player_input.bind("<Return>", self.process)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        # the image container and default image
        img = None # represents the actual image
        self.image_container = Label(self, width=Game.WIDTH // 2, image=img)
        self.image_container.image = img # ensuring image persistence after function ends
        self.image_container.pack(side=LEFT, fill=Y)
        self.image_container.pack_propagate(False) # prevent the image from modifying the size of the container it is in

        # container for the game text
        text_container = Frame(self, width=Game.WIDTH // 2)
        self.text = Text(text_container, bg="lightgrey", fg="black", state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_container.pack(side=RIGHT, fill=Y)
        text_container.pack_propagate(False)

    def set_room_image(self):
        if self.current_room == None:
            img = PhotoImage(file="images/skull.gif")
        else:
            img = PhotoImage(file=self.current_room.image)

        self.image_container.config(image=img)
        self.image_container.image = img

    def set_status(self, status):
        self.text.config(state=NORMAL) # make it editable
        self.text.delete(1.0, END) # yes 1.0 for text, 0 for entry elements

        if self.current_room == None:
            self.text.insert(END, Game.STATUS_DEAD)
        else:
            content = f"{self.current_room}\nYou are carrying: {self.inventory}\n\n{status}"
            self.text.insert(END, content)

        self.text.config(state=DISABLED) # no longer editable

    def clear_entry(self):
        self.player_input.delete(0, END)

    def handle_go(self, destination):
        status = Game.STATUS_BAD_EXIT

        if destination in self.current_room.exits:
            self.current_room =  self.current_room.exits[destination]
            status = Game.STATUS_ROOM_CHANGE

        self.set_status(status)
        self.set_room_image()


    def handle_look(self, item):
        status = Game.STATUS_BAD_ITEM

        if item in self.current_room.items:
            status = self.current_room.items[item]

        self.set_status(status)

    def handle_take(self, grabbable):
        status = Game.STATUS_BAD_GRABBABLE

        if grabbable in self.current_room.grabbables:
            self.inventory.append(grabbable)
            self.current_room.del_grabbables(grabbable)
            status = Game.STATUS_GRABBED

        self.set_status(status)

    def play(self):
        self.setup_game()
        self.setup_gui()
        self.set_room_image()
        self.set_status("")

    def process(self, event):
        action = self.player_input.get()
        action = action.lower()

        if action in Game.EXIT_ACTIONS:
            exit()

        if self.current_room == None:
            self.clear_entry()
            return
        
        words = action.split()

        if len(words) != 2:
            self.set_status(Game.STATUS_DEFAULT)
            return
        
        self.clear_entry()

        verb = words[0]
        noun = words[1]

        match verb:
            case "go": self.handle_go(destination=noun)
            case "look": self.handle_look(item=noun)
            case "take": self.handle_take(grabbable=noun)

########################### MAIN ###########################################
window = Tk()
window.title("Room Adventure... REVOLUTIONS")
game = Game(window)
game.play()
window.mainloop()