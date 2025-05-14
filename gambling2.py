import random

entries = 0
wallet = 0

grand_prize = 300000
print("\n🎰 Welcome to GetCashNow – Pick-A-Box Game 🎰")

while True:
    amount = int(input("\nEnter amount to play (50 to 2000 Ksh): "))
    if amount < 50 or amount > 2000:
        print("⛔ Amount must be between 50 and 2000 Ksh.")
        continue

    entries += 1
    print(f"Entry #{entries} - You played with {amount} Ksh")

    # Determine win
    if entries >= 25:
        win = random.choices([True, False], weights=[1, 5])[0]  # 16.6% win chance
    else:
        win = False

    # Box setup: 1 grand prize, others 0 or small values
    boxes = [0, 0, 0, 0, 0, 0]

    # Place some tempting random values in 2-3 boxes
    for _ in range(random.randint(2, 3)):
        index = random.randint(0, 5)
        if boxes[index] == 0:
            boxes[index] = random.choice([1000, 5000, 15000, 20000])

    # Assign grand prize if win is True
    if win:
        prize_index = random.randint(0, 5)
        boxes[prize_index] = grand_prize

    # User picks
    user_choice = int(input("Pick a box (1-6): ")) - 1
    user_box_value = boxes[user_choice]

    # Display outcome
    if user_box_value == 0:
        print("😢 Oops! Your box was empty.")
    elif user_box_value == grand_prize:
        print(f"🎉 JACKPOT! You won {grand_prize} Ksh!")
        break
    else:
        print(f"🎁 Congrats! Your box had {user_box_value} Ksh!")
        wallet += user_box_value

    # Mini-reward encouragement
    if entries in [14, 18, 22] and not win:
        mini_reward = random.randint(50, 200)
        wallet += mini_reward
        print(f"💡 So close! You got a bonus of {mini_reward} Ksh for your effort.")

    # Reveal other boxes
    print("\n📦 Here’s what all the boxes had:")
    for i, val in enumerate(boxes):
        tag = "<-- Your pick" if i == user_choice else ""
        print(f"Box {i+1}: {val} Ksh {tag}")

    # Continue or not
    cont = input("\nWanna try again? (y/n): ").strip().lower()
    if cont != 'y':
        break

print(f"\n💰 Game over. You earned a total of {wallet} Ksh. Thanks for playing!")
