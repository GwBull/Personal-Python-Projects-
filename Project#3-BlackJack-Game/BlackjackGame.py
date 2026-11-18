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

    
