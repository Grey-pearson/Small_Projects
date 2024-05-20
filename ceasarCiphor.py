alphabet = [
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


def begin():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("whoops, try again that didnt sound right")
        begin()


def encrypt(text, shift):
    temp_container = []
    for i in text:
        if i == " ":
            temp_container.append(" ")
        else:
            aplphabet_index = alphabet.index(i)
            aplphabet_index += shift
            if aplphabet_index >= 26:
                aplphabet_index -= 26
            coded_char = alphabet[aplphabet_index]
            temp_container.append(coded_char)
    coded_message = "".join(temp_container)
    print(coded_message)


def decrypt(text, shift):
    shift *= -1
    encrypt(text, shift)


begin()
