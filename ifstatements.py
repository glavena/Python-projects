#if it's a cold day, tell them to wear warm cloths and enjoy their day
#if it's a hot day ask them to drink lost aof water and enjoy their day
#if its neither hot nor cold wish them a lovely day
weather =input("How is the weather today? (Cold,Hot,Warm): ").strip().lower()

if weather == 'cold':
     print('Wear warm cloths')
elif weather == 'hot':
     print('Drink lots of water')
else:
     print ("It's a wonderful day")


price = 1000000
price =int(price)
customer = input('Do you have good credit? (yes/no) :').strip().lower()

if customer =='yes':
    print(f'Make a down payment of {price*0.1} dollars')
else:
    print(f'Make a down payment of {price *0.2} dollars')


