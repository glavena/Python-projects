#comparison operators when we want to compare a variable with a value
temp=38
if temp >30:
    print('It is a hot day')
else:
    print ('It is not a hot day')

user = input('Input your name: ')
attempt=3
while attempt>0:
    password = input('Input your password: ')
    if len(password) < 8:
        print('Password must be at least 8 characters')
        attempt -= 1
    elif len(password) > 25:
        print('Password should not exceed 25 characters')
        attempt -= 1
    else:
        print('Your password is strong')
        break
    if attempt >0:
      print (f'You have {attempt} attempt(s) left.\n')
    else:
      print('You have ran out of attempt(s)')