import random

print("***********************************")
print("WELCOME TO THE SLOT MACHINE")
print("***********************************")
print("You have $1000 to play with. Try your luck and see if you can hit the jackpot!")
print("if you hit three matching symbols, you win 10 times your bet amount!")
print("if you hit two matching symbols, you win 2 times your bet amount!")
print("if you hit no matching symbols, you lose your bet amount.")

symbols = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]
money = 1000

print(f"you have:${money} to play with")

while money > 0:

    print("Please enter your current bet amount")

    bet = int(input())

    if bet > money:
        print("You don't have enough money to place that bet.")
    else:
        print(f"You have placed a bet of: {bet} spinning the slot machine...")

        # Simulate the slot machine spinning
        wheel1 = random.choice(symbols)
        wheel2 = random.choice(symbols)
        wheel3 = random.choice(symbols)

        if wheel1 == wheel2 == wheel3:
            print(f"Congratulations! You hit the jackpot with {wheel1} {wheel2} {wheel3}!")
            money = money + bet * 10  # Jackpot pays 10 times the bet

        elif wheel1 == wheel2 or wheel2 == wheel3 or wheel1 == wheel3:
            print(f"You won with {wheel1} {wheel2} {wheel3}!")
            money = money + bet * 2  # Two matching symbols pay 2 times the bet

        else:
            print(f"Sorry, you lost with {wheel1} {wheel2} {wheel3}.")
            money = money - bet  # Lose the bet amount

        print("Type 'exit' to quit or press Enter to continue playing.")

    choice = input()

    if choice == "exit":
        print("Thanks for playing!")
    elif money <= 0:
        print("You have run out of money. Game over!")
    else:
        print(f"You have {money} left to play with.")

    

                   



