import random

balance = 100
while balance > 0:
    print(f"Your balance: ${balance}")
    play = input("Press enter to roll the dice...")
    roll = random.randint(1, 6)
    if roll == 6:
        print("You won $10!")
        balance += 10
    else:
        print("You lost $5.")
        balance -= 5
