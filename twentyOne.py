import random

player_hand = []


def start_game():
    # add card to player hand
    deal_card(2)
    # tell player what cards they have and what they total too
    show_hand(player_hand)
    # check if player is over 21
    check_hand(player_hand)

    deal = input("do you want another card")


def deal_card(cards):
    for i in range(cards):
        elephant = random.randint(1, 10)
        player_hand.append(elephant)
    print(player_hand)


def show_hand(player_hand):
    elephant = 0
    for i in player_hand:
        elephant += i

    print(f"you a {player_hand} totalling to {elephant}")


def check_hand(player_hand):
    elephant = 0
    for i in player_hand: 
        elephant += i
    if elephant > 21:
        # game over idk how