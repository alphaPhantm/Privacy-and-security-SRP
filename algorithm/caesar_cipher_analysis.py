def decrypt(text, shift):
    erg = ""
    char = [char for char in text]

    for i in range(len(char)):

        char[i] = ord(char[i])

        if char[i] in range(ord('a'), ord('z') + 1):

            char[i] = char[i] - int(shift)
            if char[i] < ord('a'):
                char[i] = char[i] + (ord('z') - ord('a')) + 1

        elif char[i] in range(ord('A'), ord('Z') + 1):

            char[i] = char[i] - int(shift)
            if char[i] < ord('A'):
                char[i] = char[i] + (ord('Z') - ord('A')) + 1

        elif char[i] in range(ord('0'), ord('9') + 1):

            char[i] = char[i] - int(shift)
            if char[i] < ord('0'):
                char[i] = char[i] + (ord('9') - ord('0')) + 1

        elif char[i] in range(ord(' '), ord('/') + 1):

            char[i] = char[i] - int(shift)
            if char[i] < ord(' '):
                char[i] = char[i] + (ord('/') - ord(' ')) + 1

        elif char[i] in range(ord(':'), ord('@') + 1):

            char[i] = char[i] - int(shift)
            if char[i] < ord(':'):
                char[i] = char[i] + (ord('@') - ord(':')) + 1

        char[i] = chr(int(char[i]))
        erg += char[i]

    return erg


def get_most_used_char(text):
    text = text.upper()
    anzahl = []
    for i in range(26):
        anzahl.append([text.count(chr(i+65)), chr(i+65)])

    char = max(anzahl)
    char = char[1]
    return char


def get_verschiebung(char):
    char = ord(char) - 65
    e = ord("E") - 65
    verschiebung = char - e

    return verschiebung


def hack(text):
    return decrypt(text, get_verschiebung(get_most_used_char(text)))
