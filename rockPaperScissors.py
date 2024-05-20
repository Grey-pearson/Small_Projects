import random

# ask for amount of times you want to play then call function with loop that plays game
# print('how many times do you wanna play rock paper scissors to determin the winner?')
num_games = input(
    "how many times do you wanna play rock paper scissors to determin the winner? "
)


def play_game():

    player_guess = input("guess r p s: ")

    ai_guess = random.randint(0, 2)

    who_won(player_guess, ai_guess)


def who_won(player_guess, ai_guess):
    match player_guess:
        case "r":
            if ai_guess == 0:
                print("Tie! ai guessed rock")
            elif ai_guess == 1:
                print("you lost ai picked paper")
            else:
                print("you won! ai picked scissors")
        case "p":
            if ai_guess == 1:
                print("Tie! ai guessed paper")
            elif ai_guess == 2:
                print("you lost ai picked scissors")
            else:
                print("you won! ai picked rock")
        case "s":
            if ai_guess == 2:
                print("Tie! ai guessed scissors")
            elif ai_guess == 0:
                print("you lost ai picked rock")
            else:
                print("you won! ai picked paper")


for i in range(int(num_games)):
    play_game()
