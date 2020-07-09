import sys
import textwrap

from room import Room
from player import Player
from item import Item
from init_items import init_items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", init_items["outside"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", init_items["foyer"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", init_items["overlook"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", init_items["narrow"], False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", init_items["treasure"], False),
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
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Gorgik the Liberator", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f"{player1.current_room.name}:")
    for line in textwrap.wrap(player1.current_room.description):
        print(line)
    if len(player1.current_room.items) > 0:
        print("You see: \n")
        for i in player1.current_room.items:
            print(i.name)
    cmd_input = input(">").split(" ", 1)
    cmd_start = cmd_input[0]
    if cmd_start == "q":
        sys.exit()
    elif cmd_start in ["n", "e", "s", "w"]:
        move_to = f"{cmd_start}_to"
        target_room = getattr(player1.current_room, move_to)
        if target_room:
            player1.current_room = target_room
            print(f"\n{player1.current_room.name}:")
        else:
            print("You cannot go that way.")
        continue
    # TO DO: spin of item name parser into separate function (maybe class method in another file?)
    # Then use that in both "get" and "drop"
    elif cmd_start in ["get", "take"]:
        if len(cmd_input) == 1:
            print("What would you like to take?")
            continue
        else:
            to_get = cmd_input[1]
            items_found = []
            for i in player1.current_room.items:
                if i.name.find(to_get) != -1:
                    items_found.append(i)
            if len(items_found) == 0:
                print(f"You don't see a {to_get}.")
                continue
            elif len(items_found) > 1:
                print(f"Please be more specific. You might mean:")
                for i in items_found:
                    print(i.name)
                continue
            else:
                items_found[0].on_take()
                player1.items.append(items_found[0])
                player1.current_room.items.remove(items_found[0])
                continue
    elif cmd_start == "drop":
        if len(cmd_input) == 1:
            print("What would you like to drop?")
            continue
        else:
            to_drop = cmd_input[1]
            items_found = []
            for i in player1.items:
                if i.name.find(to_drop) != -1:
                    items_found.append(i)
            if len(items_found) == 0:
                print(f"You don't have a {to_drop}.")
                continue
            elif len(items_found) > 1:
                print(f"Please be more specific. You might mean:")
                for i in items_found:
                    print(i.name)
                continue
            else:
                items_found[0].on_drop()
                player1.items.remove(items_found[0])
                player1.current_room.items.append(items_found[0])
                continue
    elif cmd_start == "i":
        if len(player1.items) == 0:
            print("You are not carrying anything.\n")
            continue
        else:
            print("You are carrying:")
            for i in player1.items:
                print(i.name)