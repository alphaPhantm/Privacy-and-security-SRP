from collections import deque


def str2num(zeichenkette):
    return deque([ord(c)-65 for c in zeichenkette])

walzen_r = ['EKMFLGDQVZNTOWYHXUSPAIBRCJ',  # I
            'AJDKSIRUXBLHWTMCQGZNPYFVOE',  # II
            'BDFHJLCPRTXVZNYEIWGAKMUSQO',  # III
            'ESOVPZJAYQUIRHXLNFTGKDCMWB',  # IV
            'VZBRGITYUPSDNHLXAWMJQOFECK',  # V
            'JPGVOUMFYQBENHZRDKASXLICTW',  # VI
            'NZJHGRCXMYSWBOUFAIVLPEKQDT',  # VII
            'FKQHTLXOCBJSPDZRAMEWNIUYGV']  # VIII
walzen_r = [deque(str2num(zeile)) for zeile in walzen_r]

walzen_l = deque(range(26))

UKWs = ['EJMZALYXVBWFCRQUONTSPIKHGD',  # UKW A
        'YRUHQSLDPXNGOKMIEBFZCWVJAT',  # UKW B
        'FVPJIAOYEDRZXWGCTKUQSBNMHL']  # UKW C
UKWs = [deque(str2num(zeile)) for zeile in UKWs]

kerbenKat = "Q E V J Z ZM ZM ZM"
kerbenKat = [deque(str2num(zeile)) for zeile in kerbenKat.split()]

class Walze():
    def __init__(self, nr, w_pos, r_pos):
        self.w_pos = w_pos
        self.r_pos = r_pos
        self.verdr_r = walzen_r[nr - 1].copy()
        self.verdr_l = walzen_l.copy()
        self.kerben = kerbenKat[nr - 1]
        self.setup()

    def setup(self):
        offset = self.r_pos - self.w_pos
        self.verdr_l.rotate(offset)
        self.verdr_r.rotate(offset)
        self.kerben = [(k - self.r_pos) % 26 for k in self.kerben]

    def show(self):
        for nr in self.verdr_l:
            print(chr(nr + 65), end="")
        print()
        for nr in self.verdr_r:
            print(chr(nr + 65), end="")
        print()
        for nr in self.kerben:
            print(chr(nr + 65), end="")
        print()

    def click(self):
        self.verdr_l.rotate(-1)
        self.verdr_r.rotate()

    def schaltung(self):


w = Walze(3, ord("T") - 65, 4)
w.show()
