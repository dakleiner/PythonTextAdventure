def instructions():  # Instructions for the game.
    print('Welcome to the Lich\'s Lair.')
    print('You have been captured by Vhekrug.')
    print('Search each room in his fortress to find your gear.')
    print('Without all items you will be turned into an undead minion.')
    print('You can move rooms by typing Move')
    print('You can search rooms by typing Search')
    print('You can check your inventory by typing Check.')
    print('You can quit anytime by typing Exit.')
    print('\nGood luck paladin')


def page_break():  # Function to create space between actions
    print('*' * 60)
    print()


# Dictionary to hold possible direction of travel and Items kept in each room.
rooms = {
    'Dungeon': {'Name': 'Dungeon',
                'South': 'Laboratory',
                'Equip': 'Clothes'},
    'Laboratory': {'Name': 'Laboratory',
                   'North': 'Dungeon',
                   'West': 'Library',
                   'Equip': 'Dagger'},
    'Library': {'Name': 'Library',
                'East': 'Laboratory',
                'North': 'Barracks',
                'West': 'Throne Room',
                'South': 'Chapel',
                'Equip': 'Spell Book'},
    'Throne Room': {'Name': 'Throne Room',
                    'East': 'Library'},
    'Barracks': {'Name': 'Barracks',
                 'East': 'Armory',
                 'South': 'Library',
                 'Equip': 'Armor'},
    'Armory': {'Name': 'Armory',
               'West': 'Barracks',
               'Equip': 'Sword'},
    'Chapel': {'Name': 'Chapel',
               'East': 'Crypt',
               'North': 'Library',
               'Equip': 'Holy Symbol'},
    'Crypt': {'Name': 'Crypt',
              'West': 'Chapel',
              'Equip': 'Shield'}
}


player_inventory = ['Clothes']  # Player inventory to track items.
player_position = rooms['Dungeon']  # Room player is currently in.
directions = ['North', 'South', 'East', 'West']  # Directions for validation.
action_list = ['Move', 'Search', 'Check', 'Exit']  # Actions for validation.

def room_desc(player_position):  # Function to add descrition for player.
    if player_position['Name'] == 'Dungeon':
        print('You are in the Dungeon. There is a door to your South.')
    elif player_position['Name'] == 'Laboratory':
        print('You have entered what seems to be a Laboratory. There are doors to the North and West.')
    elif player_position['Name'] == 'Library':
        print('You have entered an vast Library. There are doors in all directions')
    elif player_position['Name'] == 'Chapel':
        print('You have entered a desolate Chapel. There are door to the North and East')
    elif player_position['Name'] == 'Crypt':
        print('You have entered the crypt.  There is only one door to the West.')
    elif player_position['Name'] == 'Barracks':
        print('You have entered a Barracks. There are doors to the South and East.')
    elif player_position['Name'] == 'Armory':
        print('You have entered an Armory.  There is only a Door to the West')


instructions()
page_break()
room_desc(player_position)

command = input('What action will you take?:\n').title()

while command != 'Exit':  # Entry of game loop.

    if command == 'Move':  # if statement for movement command.
        player_direction = input('What direction will you go?:\n').title()  # Get direction of travel.
        if player_direction in directions:  # Next two lines are for validation.
            if player_direction in player_position:
                player_position = rooms[player_position[player_direction]]  # Change player room.
            else:
                print('Invalid direction.')

    elif command == 'Check':  # Allow player to check inventory.
        print('Items in your possession:', str(player_inventory)[1:-1].replace("'", ""))

    elif command == 'Search':  # Statement to allow player to add items to inventory.
        discovery = player_position['Equip']  # Variable used to store item to be found in room.
        if discovery not in player_inventory:  # If statement to not allow multiples in inventory.
            player_inventory.append(discovery)
            print('You have recovered your', discovery)
        else:  # Else to let player know they found all items in that room
            print('You find nothing of use.')
    else:  # Else to let player know  their action was not valid.
        print('Command invalid')

    if player_position['Name'] == 'Throne Room' and len(player_inventory) < 7:  #If statement 
        print('You have entered the lair of Vhekrug unprepared.')
        print('Even though you fought valiantly you are no match for the lich.')
        print('In the end you have been turned into one of his undead minions')
        command = 'Exit'
    elif player_position['Name'] == 'Throne Room' and len(player_inventory) > 6:
        print('You have braved the lair of Vhekrug, collecting your gear.')
        print('After a hard fought battle you manage to defeat the vile creature')
        print('He has been banished back to his phylactery, which was not located in the castle')
        command = 'Exit'
    else:
        page_break()
        room_desc(player_position)
        command = input('What action will you take?:\n').title()
