import time


def encrypt(text, key):
    erg = ""
    char_text = [int(ord(char)) for char in text]
    char_key = [int(ord(char)) for char in key]

    key_index = 0

    for i in range(len(char_key)):
        if char_key[i] in range(ord('a'), ord('z') + 1):

            char_key[i] = char_key[i] - ord('a')

        elif char_key[i] in range(ord('A'), ord('Z') + 1):

            char_key[i] = char_key[i] - ord('A')

        elif char_key[i] in range(ord('0'), ord('9') + 1):

            char_key[i] = char_key[i] - ord('0')

        elif char_key[i] in range(ord(' '), ord('/') + 1):

            char_key[i] = char_key[i] - ord(' ')

        elif char_key[i] in range(ord(':'), ord('@') + 1):

            char_key[i] = char_key[i] - ord(':')

    for i in range(len(char_text)):

        if key_index > len(key) - 1:
            key_index = 0

        if char_text[i] in range(ord('a'), ord('z') + 1):

            char_text[i] = char_text[i] + char_key[key_index]
            key_index += 1

            if char_text[i] > ord('z'):
                char_text[i] = char_text[i] - (ord('z') - ord('a')) - 1

        if char_text[i] in range(ord('A'), ord('Z') + 1):

            char_text[i] = char_text[i] + char_key[key_index]
            key_index += 1

            if char_text[i] > ord('Z'):
                char_text[i] = char_text[i] - (ord('Z') - ord('A')) - 1

        if char_text[i] in range(ord('0'), ord('9') + 1):

            char_text[i] = char_text[i] + char_key[key_index]
            key_index += 1

            if char_text[i] > ord('9'):
                char_text[i] = char_text[i] - (ord('9') - ord('0')) - 1

        if char_text[i] in range(ord(' '), ord('/') + 1):

            char_text[i] = char_text[i] + char_key[key_index]
            key_index += 1

            if char_text[i] > ord('/'):
                char_text[i] = char_text[i] - (ord('/') - ord(' ')) - 1

        if char_text[i] in range(ord(':'), ord('@') + 1):

            char_text[i] = char_text[i] + char_key[key_index]
            key_index += 1

            if char_text[i] > ord('@'):
                char_text[i] = char_text[i] - (ord('@') - ord(':')) - 1

        char_text[i] = chr(int(char_text[i]))
        erg += char_text[i]

    return erg


def decrypt(text, key):
    erg = ""
    char_text = [int(ord(char)) for char in text]
    char_key = [int(ord(char)) for char in key]

    key_index = 0

    for i in range(len(char_key)):
        if char_key[i] in range(ord('a'), ord('z') + 1):

            char_key[i] = char_key[i] - ord('a')

        elif char_key[i] in range(ord('A'), ord('Z') + 1):

            char_key[i] = char_key[i] - ord('A')

        elif char_key[i] in range(ord('0'), ord('9') + 1):

            char_key[i] = char_key[i] - ord('0')

        elif char_key[i] in range(ord(' '), ord('/') + 1):

            char_key[i] = char_key[i] - ord(' ')

        elif char_key[i] in range(ord(':'), ord('@') + 1):

            char_key[i] = char_key[i] - ord(':')

    for i in range(len(char_text)):

        if key_index > len(key) - 1:
            key_index = 0

        if char_text[i] in range(ord('a'), ord('z') + 1):

            char_text[i] = char_text[i] - char_key[key_index]
            key_index += 1

            if char_text[i] < ord('a'):
                char_text[i] = char_text[i] + (ord('z') - ord('a')) + 1

        if char_text[i] in range(ord('A'), ord('Z') + 1):

            char_text[i] = char_text[i] - char_key[key_index]
            key_index += 1

            if char_text[i] < ord('A'):
                char_text[i] = char_text[i] + (ord('Z') - ord('A')) + 1

        if char_text[i] in range(ord('0'), ord('9') + 1):

            char_text[i] = char_text[i] - char_key[key_index]
            key_index += 1

            if char_text[i] < ord('0'):
                char_text[i] = char_text[i] + (ord('9') - ord('0')) + 1

        if char_text[i] in range(ord(' '), ord('/') + 1):

            char_text[i] = char_text[i] - char_key[key_index]
            key_index += 1

            if char_text[i] < ord(' '):
                char_text[i] = char_text[i] + (ord('/') - ord(' ')) + 1

        if char_text[i] in range(ord(':'), ord('@') + 1):

            char_text[i] = char_text[i] - char_key[key_index]
            key_index += 1

            if char_text[i] < ord(':'):
                char_text[i] = char_text[i] + (ord('@') - ord(':')) + 1

        char_text[i] = chr(int(char_text[i]))
        erg += char_text[i]

    return erg


if __name__ == '__main__':

    print(encrypt("Ich Liebe dich mein Knuffi!", "Mauschen"))
    print("")
    print("")
    time.sleep(3)
    print(decrypt('Ucb"Npioq xaeo$zqih"Muysri%', "Mauschen"))