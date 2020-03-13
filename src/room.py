# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return_string = "---------"
        return_string += "\n\n"
        return_string += self.name
        return_string += "\n\n"
        return_string += self.description
        return_string += "\n\n"
        if len(self.items) > 0:
            return_string += f"There are some items in this room!\n{self.items}\n\n"
        else:
            return_string += "There are no items in this room"
        return_string += "\n\n"
        return_string += f"Directions you can travel: {self.get_exits_string()}"
        return return_string

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

    def take_item(self, item):
        try:
            item_index = self.items.index(item)
            self.items.pop(item_index)
            return True
        except:
            return False

    def add_to_items(self, item):
        self.items.append(item)

    # def remove_from_inventory(self, item):
    #     # search if the item is in the inventory and if so, at what index
    #     try:
    #         self.items.index(item)
    #     except:
    #         print(f"There isn't a {item} in this room")
    #         return None
    #     # if the item is in the inventory, remove it
