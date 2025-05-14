# car game
car_start = False
print ('Welcome to the game')
while True:

    user = input ('(START/STOP/EXIT)').strip().lower()
    if user =='start':
        if car_start:
            print ('game has already started')
        else:
            car_start = False
            print ('game has started')

    elif user =='stop':
        if not car_start:
            print ('game has already stopped')
        else:
            car_start = False
            print('game has stopped')

    elif user =='exit':
        print ('you have exited the game')
        break
    else:
        print ('cmd not understood')





