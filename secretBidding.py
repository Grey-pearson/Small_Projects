# function to add players and their bids and the value in to a dict
# function to calculate winner
# function to start bidding

bidders = {}


def start_bidding():
    print(
        "Welcome to seceret bidding, each partisipant will bid individually and then the winner will be anounced at the end"
    )
    add_player()
    print(bidders)

    who_wins()


def add_player():
    print("whats your players name?")
    name = input()
    print(f"how much would you like to bid {name}")
    bid = input()
    # add info to bidders
    bidders.setdefault(name, bid)

    print("is there another bidder? y/n")
    answer = input()
    answer.lower()
    if answer == "y":
        # try calling this function again ig?
        add_player()


def who_wins():
    for players in bidders:
        


start_bidding()
