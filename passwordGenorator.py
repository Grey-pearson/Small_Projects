import random

# ask for total length of password
# ask how many letters user wants
# ask how many numbers user wants
# ask how many symbols user wants

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
capital_letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "-",
    "+",
    "=",
    "?",
    "/",
    ":",
    ";",
]


def start_generation():
    print("Welcome to the password generator!")
    # save how many of each char type is needed, randomly select the correct num of each char
    # and assign it to temp container, then move them all to a new contaier but in a random order
    # do the bag method like in tetris so delete each char pulled after assigning it to the new container
    # use method to make it one string and print as new password
    temp_password = []
    password = []

    print(
        "how many lower case letters do you want in your password? use just numbers: "
    )
    num_letters = int(input())

    print(
        "how many upper case letters do you want in your password? use just numbers: "
    )
    num_capitals = int(input())

    print("how many numbers do you want in your password? use just numbers: ")
    num_nums = int(input())

    print("how many symbols do you want in your password? use just numbers: ")
    num_symbols = int(input())

    """print(num_letters)
    print(num_capitals)
    print(num_nums)
    print(num_symbols)"""

    for char in range(num_letters):
        temp_password.append(random.choice(letters))
    for char in range(num_capitals):
        temp_password.append(random.choice(capital_letters))
    for char in range(num_nums):
        temp_password.append(random.choice(numbers))
    for char in range(num_symbols):
        temp_password.append(random.choice(symbols))

    print(temp_password)
    random.shuffle(temp_password)
    print(temp_password)

    password = ""
    for char in temp_password:
        password += char

    print(password)


start_generation()
