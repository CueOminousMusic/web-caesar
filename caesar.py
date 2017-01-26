import string

def encrypt(text, rot):
    output = ""
    for char in text:
        output = output+rotate_character(char, rot)
    return output


def alphabet_position(letter):
    letter = letter.lower()
    alphabet = string.ascii_lowercase

    index = 0
    for char in alphabet:
        if letter == char:
            return index
        index += 1


def rotate_character(char, rot):
    if char not in string.ascii_letters:
        output = char
    else:
        initPosition = alphabet_position(char)
        newPosition = (initPosition + rot) % 26
        if char in string.ascii_uppercase:
            upper = True
            output = string.ascii_uppercase[newPosition]
        else:
            upper = False
            output = string.ascii_lowercase[newPosition]
    return output
