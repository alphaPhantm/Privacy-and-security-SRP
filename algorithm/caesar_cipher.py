def encrypt(text, shift):

    erg = ""
    char = [char for char in text]

    for i in range(len(char)):

        char[i] = ord(char[i])

        if char[i] in range(ord('a'), ord('z') + 1):

            char[i] = char[i] + int(shift)
            if char[i] > ord('z'):
                char[i] = char[i] - (ord('z') - ord('a')) - 1

        elif char[i] in range(ord('A'), ord('Z') + 1):

            char[i] = char[i] + int(shift)
            if char[i] > ord('Z'):
                char[i] = char[i] - (ord('Z') - ord('A')) - 1

        elif char[i] in range(ord('0'), ord('9') + 1):

            char[i] = char[i] + int(shift)
            if char[i] > ord('9'):
                char[i] = char[i] - (ord('9') - ord('0')) - 1

        elif char[i] in range(ord(' '), ord('/') + 1):

            char[i] = char[i] + int(shift)
            if char[i] > ord('/'):
                char[i] = char[i] - (ord('/') - ord(' ')) - 1

        elif char[i] in range(ord(':'), ord('@') + 1):

            char[i] = char[i] + int(shift)
            if char[i] > ord('@'):
                char[i] = char[i] - (ord('@') - ord(':')) - 1


        char[i] = chr(int(char[i]))
        erg += char[i]

    return erg


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
