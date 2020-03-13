# Creates Room Class
class Room:
    # Sets attributes for the room
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        # creates an empty list to hold the items in the room. default to no items.
        # items will be added when the room instances are made
        self.items = []

    # method that runs when print(player.current_room) is called.
    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += self.name
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        # conditional to print a different thing on this line depending on whether there are any items in the self.items list
        if len(self.items) > 0:
            return_string += f"There are some items in this room!\n{self.items}\n\n"
        else:
            return_string += "There are no items in this room"
        return_string += "\n\n"
        return_string += f"Directions you can travel: {self.get_exits_string()}"
        return return_string

    # checks for the available directions of from the current room and saves them to a list.
    # returns that list
    def get_exits_string(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits

    # method called from the player class when trying to take an item from the room
    def take_item(self, item):
        # checks if the item is in the room's item list
        # if so, removes the item from the rooms list and returns true so that the player's method can continue
        # if not, returns false so the player's method can return correct response
        try:
            item_index = self.items.index(item)
            self.items.pop(item_index)
            return True
        except:
            return False

    # adds a given item to the room's item list
    def add_to_items(self, item):
        self.items.append(item)
