# Car Game
car_start = False
print('Welcome to the game')

while True:
    user = input('(START/STOP/EXIT): ').strip().lower()

    if user == 'start':
        if car_start:
            print('Game has already started')
        else:
            car_start = True
            print('Game has started')

    elif user == 'stop':
        if not car_start:
            print('Game has already stopped')
        else:
            car_start = False
            print('Game has stopped')

    elif user == 'exit':
        print('You have exited the game')
        break

    else:
        print('Command not understood')
