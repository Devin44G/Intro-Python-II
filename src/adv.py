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

room['outside'].add_item('sword')

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


player = Player(room['outside'])


def try_direction(player, direction):
    attr = direction + '_to'

    if hasattr(player.curr_location, attr):
        player.curr_location = getattr(player.curr_location, attr)
    else:
        print('You can\'t go in that direction!')


# THE GAME LOOP
playing = True

while playing:
    # PRINTS PLAYER'S CURRENT LOCATION EACH TIME LOOP IN INVOKED
    print(f'\n {player.curr_location.description} \n')

    # WAITING FOR PLAYER INPUT
    player_input = input(
        '''\n
        Where do you want to go?
        Choose [n]:North, [s]:South, [e]:East, [w]:West . . .
        Or press [q] to quit!\n
        ''').lower().split(' ')

    # IF PLAYER DOESN'T INPUT ANYTHING
    if len(player_input) == 0:
        print('Please choose a direction')

    if len(player_input) == 1:
        if player_input[0] == 'q':
            print('You have quit the game. See ya next time!')
            playing = False
        elif player_input[0] == 'n':
            try_direction(player, player_input[0])
        elif player_input[0] == 's':
            try_direction(player, player_input[0])
        elif player_input[0] == 'e':
            try_direction(player, player_input[0])
        elif player_input[0] == 'w':
            try_direction(player, player_input[0])
        elif player_input[0] == 'i':
            player.check_inv()

    if len(player_input) > 1:
        if player_input[0] == 'take':
            # print(player_input)
            for item in player.curr_location.items:
                if player_input[1] == item:
                    player.take_item(item)
                    player.curr_location.remove_item(item)
                    print(player.curr_location.items, player.inventory)
