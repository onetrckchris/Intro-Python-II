from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
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

def die():
    return "\n--- Your vision goes hazy and in an instant you fall to the ground... Lifeless.\nPlease only select from valid inputs.\n"

player_name = input("Please enter your name: ")

player1 = Player(player_name, room['outside']) # Creating the player. They start outside always.

print(f"\n\nWelcome to my adventure game, {player1.name}!")
print(f"--- You're currently at the {player1.current_room.name.lower()}.")
print(f"----- {player1.current_room.description}")

# Doing it the super inefficient way first. Just to get this done.
user_input = input("[w] Walk forth to the foyer...\n[q] -- Quit game --\n: ")
while user_input != 'q':
    # (Outside) Player walks north to the foyer.
    if user_input == 'w':
        player1.current_room = room['foyer']
        print(f"\n--- You're currently at the {player1.current_room.name.lower()}.")
        print(f"----- {player1.current_room.description}")
        user_input = input("[w] Walk up the stairs through the north passage.\n[d] Make your way through the seemingly narrow east passage.\n[s] Head back to the cave entrance.\n[q] -- Quit game --\n: ")
        # (Foyer) Player walks north to the overlook.
        if user_input == 'w':
            player1.current_room = room['overlook']
            print(f"\n--- You're currently at the {player1.current_room.name.lower()}.")
            print(f"----- {player1.current_room.description}")
            user_input = input("[s] Walk back to the foyer.\n[q] -- Quit game --\n: ")
            # (Overlook) Player walks south to foyer.
            if user_input == 's':
                player1.current_room = room['foyer']
                print(f"\n--- You're currently at the {player1.current_room.name.lower()}.")
                print(f"----- {player1.current_room.description}")
                user_input = input("[w] Walk up the stairs through the north passage.\n[d] Make your way through the seemingly narrow east passage.\n[s] Head back to the cave entrance.\n[q] -- Quit game --\n: ")
        # (Foyer) Player walks east through the narrow passage.
        elif user_input == 'd':
            player1.current_room = room['narrow']
            print(f"\n--- You're currently walking through a {player1.current_room.name.lower()}.")
            print(f"----- {player1.current_room.description}")
            user_input = input("[w] Follow the smell of gold.\n[a] Walk back to the foyer.\n[q] -- Quit game --\n: ")
            if user_input == 'w':
                player1.current_room = room['treasure']
                print(f"\n--- You're currently in the {player1.current_room.name.lower()}.")
                print(f"----- {player1.current_room.description}")
                print("\nSorry about no treasure! :( But you beat the game, good job!")
                break
        # (Foyer) Player walks south back outside.
        elif user_input == 's':
            player1.current_room = room['outside']
            print(f"\n--- You're currently at the {player1.current_room.name.lower()}.")
            print(f"----- {player1.current_room.description}")
            user_input = input("[w] Walk forth to the foyer...\n[q] -- Quit game --\n: ")
    else:
        print(die())
        break