# ask user name
# randomly pick a word from array
# ask user for char they think could be in word
# if yes dispay that letter as proggress to guessing word
# if no tell them its not in the word

import random
import sys

words = [
    "rainbow",
    "computer",
    "science",
    "programming",
    "python",
    "mathematics",
    "player",
    "condition",
    "reverse",
    "water",
    "board",
    "geeks",
]

# word player has to guess
word = random.choice(words)
# so i can check for chars and other stuff
arrWord = []
for i in word:
    arrWord.append("_")

# how many guesses its taken
# guesses = 0

print("ok dawg, the word you gotta guess is " + str(len(word)) + " long")

charLeft = 0
guesses = 0

# while loop for game loop - infinity
# display arrWord.len() as new var arrWord thats all '_'
# ask for letter guess
# for arrWord compair if letter is found
# if yes update arrWord at arrWord[i] with the letter

while True:
    # tracking gusses

    # showing how many chars have been sucessfully gussed
    print(" ".join(arrWord))
    print(str(guesses) + " guesses, guess a new char: ")
    charGuess = input()
    guesses += 1

    # checking and replacing chars in arrword to show what letters you have guessed correctly
    for i in range(len(word)):
        # checking each char to see if guess is right or wrong
        if charGuess == word[i]:
            arrWord[i] = charGuess

        # maybe look through word with i and if a '_' then pass but if no '_' then print words and sys.exit()
        if arrWord[i] == "_":
            charLeft += 1

    if charLeft == 0:
        print("you won!!! only took " + str(guesses) + " guesses!")
        sys.exit()
    # restting charleft to get accurate count each round
    charLeft = 0
