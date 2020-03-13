from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Take the treasure and drop it outside the mouth of the cave!"""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#

# add items to rooms
room['outside'].items = ['torch']
room['treasure'].items = ['treasure']

# Main
#

directions = ('n', 's', 'e', 'w')

# Make a new player object that is currently in the 'outside' room.
adventurer = Player("Link", room['outside'])


def check_win():
    try:
        treasure_index = room['outside'].items.index('treasure')
        if treasure_index >= 0:
            print(
                "\n\n\n~~~~~~~~~~\n\nYou got the treasure out and won the game!!!!\n\n~~~~~~~~~~")
    except:
        return None


print("\n~~~~Welcome to the Adventure Game~~~\n")
print(
    f"You are {adventurer.current_room.name}\n\n{adventurer.current_room.description}\n\n")
print(f"It looks dark in the cave, but there is a torch leaning against the entrance\n\n")
print("Type 'take torch' to pick it up, then proceed north by typting 'n'.\n\n")
while True:
    try:
        treasure_index = room['outside'].items.index('treasure')
        if treasure_index >= 0:
            print(
                "\n\n\n~~~~~~~~~~\n\nYou got the treasure out and won the game!!!!\n\n~~~~~~~~~~")
            break
    except:
        print(f"Inventory: {adventurer.inventory}")
        cmd = input("---> ")
        if cmd == "q":
            print("Quitting the game. See you later!")
            break
        elif cmd in directions:
            adventurer.travel(cmd)
        elif cmd.split()[0] == "take" and len(cmd.split()) < 3:
            if len(cmd.split()) < 2:
                print("You need to specify the item you want to take")
            else:
                adventurer.add_to_inventory(cmd.split()[1])
        elif cmd.split()[0] == "drop" and len(cmd.split()) < 3:
            if len(cmd.split()) < 2:
                print("You need to specify the item you want to drop")
            else:
                adventurer.remove_from_inventory(cmd.split()[1])
        else:
            print("\n\nSorry, I don't know that command.\n ----------")
