from room import Room

# Creates Player Class


class Player:
    # Sets the attributes for the player. Name and current_room are required arguments when a player instance is called.
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        # creates an empty list to hold items the player picks up
        self.inventory = []

    # method to move the player between rooms
    def travel(self, direction):
        # checks if the current room has a possible room bound to the given cardinal direction.
        if getattr(self.current_room, f"{direction}_to"):
            # if so, sets current room to that new room in that direction
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("You cannot move in that direction")

    # Method to add an item to inventory. "take item"
    def add_to_inventory(self, item):
        # calls the take_item method from the room class and sees if it returns True
        if self.current_room.take_item(item) is True:
            # adds the item string passed into this method to the inventory list created above in tis player class
            self.inventory.append(item)
            print(self.current_room)
        else:
            print(f"There is no {item} in this room")

    # Method to remove and item from the inventory. "drop item"
    def remove_from_inventory(self, item):
        # search if the item is in the inventory.
        try:
            # finds the item index
            item_index = self.inventory.index(item)
            # removes the item from player inventory
            self.inventory.pop(item_index)
            # adds the item to room item list
            self.current_room.items.append(item)
            print(f"\n\n{item} dropped!\nInventory ->{self.inventory}\n")
            print(self.current_room)
        # if the item doesn't exist in player inventory, inventory.index() will throw an error. In this case, the 'except' will run
        except:
            print(f"There is no {item} in your inventory")
            return None
