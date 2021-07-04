from algorithm import caesar_cipher, skytale, vigenere_cipher, enigma_V2


def control(encryption_id, text, shift, passPhrase, ukw, walze1, walze2, walze3, walzenPos, ringPosW1, ringPosW2, ringPosW3, steckerbrett):

    encryption_id = int(encryption_id)
    shift = int(shift)


    erg = ""

    if encryption_id == 0:
        erg = caesar_cipher.encrypt(text, shift)
    elif encryption_id == 1:
        erg = caesar_cipher.decrypt(text, shift)
    elif encryption_id == 2:
        erg = skytale.skytale_encrypt(text, shift)
    elif encryption_id == 3:
        erg = skytale.skytale_decrypt(text, shift)
    elif encryption_id == 4:
        erg = vigenere_cipher.encrypt(text, passPhrase)
    elif encryption_id == 5:
        erg = vigenere_cipher.decrypt(text, passPhrase)
    elif encryption_id == 6:
        erg = enigma_V2.run(ukw, walze1, walze2, walze3, walzenPos, ringPosW1, ringPosW2, ringPosW3, steckerbrett, text)

    return erg
