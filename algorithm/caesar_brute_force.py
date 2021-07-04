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
    text = text.split()
    word = word.split()
    start = time.time()

    for w in text:
        for i in range(26):
            for s in word:
                if decrypt(w, i) == s:
                    erg.append(decrypt(w, i))

    end = time.time()
    time = end - start

    return erg, time


print(brutforce("Bei der Ermittlung von Laufzeiten ist weiter zu bedenken, dass der Prozessor auch von anderen Aufgaben in Anspruch genommen wird, so dass wir gerade zwar die während des Laufs verstrichene Zeit bestimmt haben, nicht aber die Zeit, die der Prozessor hierfür tatsächlich aufgewendet hat. Dies illustrieren wir im folgenden Beispiel, in dem wir das Skript zeitweilig pausieren lassen. Damit wird in Zeile 9 simuliert, dass andere Prozesse für eine Unterbrechung der Ausführung unseres Skripts sorgen. Außerdem benutzen wir in den Zeilen 5 und 11 time.process_time(), um die vom Prozessor aufgewandte Zeit für den Prozess zu bestimmen, in dem unser Skript abgearbeitet wird.", "Prozessor Skript "))
