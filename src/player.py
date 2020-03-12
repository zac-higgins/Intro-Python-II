# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


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
        if self.current_room.take_item(item) is True:
            self.inventory.append(item)
            print(
                f"\n\n{item} added to inventory!\nInventory ->{self.inventory}\n")
            print(self.current_room)
        else:
            print(f"There is no {item} in this room")
        print(f"Inventory ->{self.inventory}")

    def remove_from_inventory(self, item):
        # search if the item is in the inventory and if so, at what index
        try:
            item_index = self.inventory.index(item)
            self.inventory.pop(item_index)
            self.current_room.items.append(item)
            print(f"\n\n{item} dropped!\nInventory ->{self.inventory}\n")
            print("current room?", self.current_room)
        except:
            print(f"There is no {item} in your inventory")
            return None
        # if the item is in the inventory, remove it
