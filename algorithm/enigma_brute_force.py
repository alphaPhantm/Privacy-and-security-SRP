
from collections import deque
from random import random


def str2num(zeichenkette):
    return [ord(c) - 65 for c in zeichenkette]


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
UKWs = [str2num(zeile) for zeile in UKWs]

kerbenKat = "Q E V J Z ZM ZM ZM"
kerbenKat = [str2num(zeile) for zeile in kerbenKat.split()]


class Walze():
    def __init__(self, nr, w_pos, r_pos):
        self.w_pos = w_pos
        self.r_pos = r_pos
        self.verdr_r = walzen_r[nr].copy()
        self.verdr_l = walzen_l.copy()
        self.kerben = kerbenKat[nr]
        self.setup()

    def setup(self):
        offset = self.r_pos - self.w_pos
        self.verdr_l.rotate(offset)
        self.verdr_r.rotate(offset)
        self.kerben = [(k - self.r_pos) % 26 for k in self.kerben]

    def click(self):
        self.verdr_l.rotate(-1)
        self.verdr_r.rotate(-1)

    def schaltung(self):
        return self.verdr_l[0] in self.kerben


class Enigma():
    def __init__(self):
        self.walzen = []
        self.ukw = []
        self.steckerbr = {}

    def setup(self, nr_ukw, nr_walzen, w_pos, r_pos, paare_steckerbr):
        for i, nr in enumerate(nr_walzen):
            wpos = ord(w_pos[i]) - 65
            rpos = r_pos[i] - 1
            self.walzen.append(Walze(nr - 1, wpos, rpos))
        self.ukw = UKWs[nr_ukw - 1]
        for a, b in paare_steckerbr.split():
            self.steckerbr[ord(a) - 65] = ord(b) - 65
            self.steckerbr[ord(b) - 65] = ord(a) - 65

    def rotiere(self):
        links, mitte, rechts = self.walzen
        if mitte.schaltung():
            mitte.click()
            links.click()
        elif rechts.schaltung():
            mitte.click()
        rechts.click()


def umwandeln(e, text):
    u_text = ""
    text = text.upper()
    for c in text:
        c = ord(c) - 65
        if c < 0 or c > 26: continue
        e.rotiere()
        c = e.steckerbr.get(c, c)
        for w in reversed(e.walzen):
            c = w.verdr_r[c]
            c = w.verdr_l.index(c)
        c = e.ukw[c]
        for w in e.walzen:
            c = w.verdr_l[c]
            c = w.verdr_r.index(c)
        c = e.steckerbr.get(c, c)
        u_text += chr(c + 65)
    return u_text



def run(ukw, walze1, walze2, walze3, walzenPos, ringPosW1, ringPosW2, ringPosW3, steckerbrett, text):

    ukw = int(ukw)
    walze1 = int(walze1)
    walze2 = int(walze2)
    walze3 = int(walze3)
    ringPosW1 = int(ringPosW1)
    ringPosW2 = int(ringPosW2)
    ringPosW3 = int(ringPosW3)

    walzen = [walze1, walze2, walze3]
    ringPos = [ringPosW1, ringPosW2, ringPosW3]

    enigma = Enigma()
    enigma.setup(ukw, walzen, walzenPos, ringPos, steckerbrett)
    erg = umwandeln(enigma, text)
    return erg


def bruteforce(text, word, steckerbrett):
    import time
    word = word.upper()
    walzen_pos = []

    for a in range(26):
        for b in range(26):
            for c in range(26):
                walzen_pos.append(chr(a+65) + chr(b+65) + chr(c+65))
    ergC = []
    wordC = []
    for c in word:
        wordC.append(c)

    start = time.time()
    for ukw in range(1, 4):
        for walze1 in range(1, 9):
            for walze2 in range(1, 9):
                for walze3 in range(1, 9):
                    for pos in walzen_pos:
                        for ringPosW1 in range(1, 27):
                            for ringPosW2 in range(1, 27):
                                for ringPosW3 in range(1, 27):
                                    erg = run(ukw, walze1, walze2, walze3, pos, ringPosW1, ringPosW2, ringPosW3, steckerbrett, text)

                                    ergC = []

                                    for c in erg:
                                        ergC.append(c)

                                    for i in range(len(ergC) - len(wordC) + 1):
                                        z = ergC[i: len(wordC) + i]
                                        s = "".join(z)

                                        if s == word:
                                            end = time.time()
                                            time = end - start
                                            #print(i)
                                            #print("UKW", ukw)
                                            #print("walze 1", walze1)
                                            #print("walze 2", walze2)
                                            #print("walze 3", walze3)
                                            #print("walzenPos", pos)
                                            #print("walzeRing1", ringPosW1)
                                            #print("walzeRing2", ringPosW2)
                                            #print("walzeRing3", ringPosW3)
                                            #print(time)
                                            #print("Finised")
                                            #exit(0)

                                            return ukw, walze1, walze2, walze3, pos, ringPosW1, ringPosW2, ringPosW3, steckerbrett, text

#Fehlt noch die Text Bearbeitung

def getText(text, word, steckerbrett):
    ukw, walze1, walze2, walze3, pos, ringPosW1, ringPosW2, ringPosW3, steckerbrett, text = bruteforce(text, word, steckerbrett)
    return(run(ukw, walze1, walze2, walze3, pos, ringPosW1, ringPosW2, ringPosW3, steckerbrett, text))
