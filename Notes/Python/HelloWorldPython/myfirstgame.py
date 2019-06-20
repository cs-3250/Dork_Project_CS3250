print('\n\n\n')

"""def room(list):
    list = ['Field', 'Forrest', 'House', 'Path']
    coords = [1,2,3,4]
    return list"""
    
def start():
    boarder = '\n#####################################################################'
    print(boarder)
    print("Hello, you are now playing the Zork 'like' Game, what would you like to do?")
    print("\nPress 1 to go to the Field")
    #print('\nPress 2 to go to the Forrest')
    #print('\nPress 3 to go to the House')
    #print('\nPress 4 to go to the Path')
    print(boarder)
    
    selection = int(input('\n---> What do you want to do? : '))
    if selection == 1:
        print(boarder)
        print("\nYou are standing in a field.\n\n1. You are dead",
              "\n2. You see a golden monkey")
        print(boarder)
        selection = int(input('\n---->1 or 2? : '))
        if selection == 1:
            print(boarder)
            print('\nBang!!! Youre are dead, goodbye!')
        elif selection == 2:
            print(boarder)
            print('\nYou pick up the golden chimp and notice that its very heavy')
            print(boarder)
            print('\n1. Sell it. \n2. Use it as a hat?')
            selection = int(input('\n---->1 or 2? : '))
            if selection == 2:
                print(boarder)
                print('\nCongradulations, you are now rich and have to pay the government for what you found!')
            elif selection == 1:
                print(boarder)
                print('You now have a very heavy fashionable new golden monkey hat')
    if selection == 2:
        print('\nYou are standing in a Forrest')
    if selection == 3:
        print('\nYou standing in front of a house')
        selection = int(input('\nWhat else do you want to do? 1 or 2? : '))
        if selection == 1:
            print('\nYou are dead')
        elif selection == 2:
            print(' You have collecteed the golden monkey and wants to play.')
    if selection == 4:
        print('You are standing in a long winding path')
        
start()


    
    
    
""" """