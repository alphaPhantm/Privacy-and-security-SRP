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

def brutforce(text, word):
    import time

    erg = []
    wordC = []
    shift = 0
    orgWord = word
    orgText = text


    for c in word:
        wordC.append(c)

    text = text.split()
    word = word.split()
    start = time.time()

    for w in text:
        for i in range(26):
            for s in word:
                massage = decrypt(w, i)
                char = []
                for c in massage:
                    char.append(c)
                for b in range(len(char) - len(wordC) + 1):
                    z = char[b: len(wordC) + b + 1]
                    s = "".join(z)

                    if s == orgWord:
                        end = time.time()
                        time = end - start
                        shift = i

    text = str(text)
    erg = decrypt(orgText, shift)
    string = "Schlüssel: " + str(shift), " in ", str(time), "s gefunden. Text: ", str(erg)
    x = "".join(string)
    return x
