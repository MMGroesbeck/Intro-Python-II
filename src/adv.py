import sys
import textwrap

import parsers

from room import Room
from player import Player
from item import Item

from init_items import init_items
from init_rooms import room

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
    print("\n")
    is_light = player1.current_room.is_light
    for i in player1.current_room.items:
        if i.light_source == True:
            is_light = True
    for i in player1.items:
        if i.light_source == True:
            is_light = True
    if is_light == True:
        for line in textwrap.wrap(player1.current_room.description):
            print(line)
        if len(player1.current_room.items) > 0:
            print("\nYou see:")
            for i in player1.current_room.items:
                print(i.name)
    else:
        print("It's too dark to see!")
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
            matches = parsers.name_in_list(cmd_input[1], player1.current_room.items)
            if matches["find_any"] == False:
                print(f"You don't see a {cmd_input[1]}.")
                continue
            elif matches["more_spec"]:
                print("Please be more specific. Which did you want to take?")
                for i in matches["found"]:
                    print(i.name)
                continue
            else:
                matches["found"][0].on_take()
                player1.items.append(matches["found"][0])
                player1.current_room.items.remove(matches["found"][0])
                continue
    elif cmd_start == "drop":
        if len(cmd_input) == 1:
            print("What would you like to drop?")
            continue
        else:
            matches = parsers.name_in_list(cmd_input[1], player1.items)
            if matches["find_any"] == False:
                print(f"You don't have a {cmd_input[1]}.")
                continue
            elif matches["more_spec"]:
                print("Please be more specific. Which did you want to drop?")
                for i in matches["found"]:
                    print(i.name)
                continue
            else:
                matches["found"][0].on_drop()
                player1.items.remove(matches["found"][0])
                player1.current_room.items.append(matches["found"][0])
                continue
    elif cmd_start == "i":
        if len(player1.items) == 0:
            print("You are not carrying anything.")
            continue
        else:
            print("You are carrying:")
            for i in player1.items:
                print(i.name)