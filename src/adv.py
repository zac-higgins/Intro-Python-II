from room import Room
from player import Player

# Declare all the rooms
room = {
    'outside':  Room("Outside the Cave Entrance",
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

# add default items to rooms
room['outside'].items = ['torch']
room['treasure'].items = ['treasure']

# sets the direction commands the player can use
directions = ('n', 's', 'e', 'w')

# Make a new player object that is currently in the 'outside' room.
adventurer = Player("Link", room['outside'])

# Welcome message that prints when the game is launched
print("\n~~~~Welcome to the Adventure Game~~~\n")
print(
    f"You are {adventurer.current_room.name}\n\n{adventurer.current_room.description}\n\n")
print(f"It looks dark in the cave, but there is a torch leaning against the entrance\n\n")
print("Type 'take torch' to pick it up, then proceed north by typting 'n'.\n\n")

# REPL Loop
while True:
    # Checks if the treasure has been dropped outside the cave entrance. If so, player wins and game exits.
    try:
        treasure_index = room['outside'].items.index('treasure')
        if treasure_index >= 0:
            print(
                "\n\n\n~~~~~~~~~~\n\nYou got the treasure out and won the game!!!!\n\n~~~~~~~~~~")
            break
    # Loops through and prints the player inventory, asks for player input command, after each command is given
    except:
        print(f"Inventory: {adventurer.inventory}")
        cmd = input("---> ")
        # command to quit the game
        if cmd == "q":
            print("Quitting the game. See you later!")
            break
        # movement commands
        elif cmd in directions:
            adventurer.travel(cmd)
        # take item commands. User types "take item_name"
        # only takes 2 word commands right now.
        elif cmd.split()[0] == "take" and len(cmd.split()) < 3:
            # catches if user just types take with no item name
            if len(cmd.split()) < 2:
                print("You need to specify the item you want to take")
            # passes just the item name to the player add_to_inventory method
            else:
                adventurer.add_to_inventory(cmd.split()[1])
        # drop item commands. User types "drop item_name"
        # only takes 2 word commands right now.
        elif cmd.split()[0] == "drop" and len(cmd.split()) < 3:
            # catches if user just types drop with no item name
            if len(cmd.split()) < 2:
                print("You need to specify the item you want to drop")
            # passes just the item name to the player remove_from_inventory method
            else:
                adventurer.remove_from_inventory(cmd.split()[1])
        # catches if the player enters anything other than the specified commands
        else:
            print("\n\nSorry, I don't know that command.\n ----------")
