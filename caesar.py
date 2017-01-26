def alphabet_position (letter):
    if letter.islower():
        position=ord(letter)-97
    if letter.isupper():
        position=ord(letter)-65

    return position


def rotate_character(char, rot):
    if not char.isalpha():
        return char
    else:
        if char.islower():
            newposition = (alphabet_position(char)+int(rot))%26+97
        if char.isupper():
            newposition = (alphabet_position(char)+int(rot))%26+65
        return chr(newposition)

def encrypt (text,rot):
    newtext=""
    for achar in text:
        newachar=rotate_character(achar,rot)
        newtext=newtext+newachar
    return newtext
