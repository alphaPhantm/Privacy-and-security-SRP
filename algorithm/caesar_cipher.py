def encrypt(text, shift):

    erg = ""
    char = [char for char in text]

    for i in range(len(char)):
        char[i] = ord(char[i])
        char[i] = char[i] + int(shift)
        char[i] = chr(int(char[i]))
        erg += char[i]

    return erg


def decrypt(text, shift):

    erg = ""
    char = [char for char in text]

    for i in range(len(char)):
        char[i] = ord(char[i])
        char[i] = char[i] - int(shift)
        char[i] = chr(int(char[i]))
        erg += char[i]

    return erg
