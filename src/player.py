# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to"):
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("You cannot move in that direction")

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        # search if the item is in the inventory and if so, at what index
        try:
            self.inventory.index(item)
        except:
            print(f"You don't have {item}")
            return None
        # if the item is in the inventory, remove it
