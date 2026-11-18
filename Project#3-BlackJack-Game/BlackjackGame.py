import random


logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

print("Welcome to Blackjack!")
print("do you want to play a game of Blackjack? Type 'y' or 'n': ")

choice = input().lower()

if choice == 'y':
    print("Great! Let's start the game.")
    # Add your game logic here
    dealer_hand = []
    ##create the dealer hand and player hand
    player_hand = []

    player_score = 0

    dealer_hand.append(random.randint(1, 11))

    player_hand.append(random.randint(1, 11))
    player_hand.append(random.randint(1, 11))
    ## assigns the player score to the sum of the player hand
    ## a random number between 1 and 11 is added to the dealer hand and player hand

    if sum(player_hand) == 21:
        print("Blackjack! You win! 🥳")
    else:
        print("You didn't get a Blackjack.")

    print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    print("Type 'y' to get another card, type 'n' to pass: ")

    if input().lower() == 'y':
        player_hand.append(random.randint(1, 11))
        print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")

        if sum(player_hand) > 21:
            print("you went over. You lose 😭")
        elif sum(player_hand) == 21:
            print("You got 21! You win! 🥳")
        else:
            print("Type 'y' to get another card, type 'n' to pass: ")
            print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
            

        

    
    
