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
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

player = Player(room['outside'])

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
def game_loop():
    print(f'\n {player.curr_location} \n')

    player_input = input(
        '''\n
        Where do you want to go?
        Choose [n]:North, [s]:South, [e]:East, [w]:West . . .
        Or press [q] to quit!\n
        ''').lower()

    if len(player_input) == 0:
        print('Please choose a direction')
        game_loop()

    if len(player_input) == 1:
        if player_input == 'q':
            print('You have quit the game. See ya next time!')
        elif player_input == 'n':
            player.curr_location = player.curr_location.n_to
            game_loop()
        elif player_input == 's':
            player.curr_location = player.curr_location.s_to
            game_loop()
        elif player_input == 'e':
            player.curr_location = player.curr_location.e_to
            game_loop()
        elif player_input == 'w':
            player.curr_location = player.curr_location.w_to
            game_loop()
        else:
            print('You can\'t go that direction!')


game_loop()

# print(room['outside'])
