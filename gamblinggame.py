import random

boxes =[0,0,102540,78765,0,0]
random.shuffle(boxes)

print ('Welcome to GetCashNow.Pick a box from 1-6: ')
user_choice =int (input ('Your Choice:')) -1 #

user_winnings = boxes [user_choice]

print('Opps your box was empty. Try again')


