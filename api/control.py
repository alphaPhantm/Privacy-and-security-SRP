from algorithm import caesar_cipher, skytale, vigenere_cipher, enigma_V2, caesar_brute_force, caesar_cipher_analysis, enigma_brute_force

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
    elif encryption_id == 7:
        erg = caesar_brute_force.brutforce(text, str(passPhrase))
    elif encryption_id == 8:
        erg = caesar_cipher_analysis.hack(text)
    elif encryption_id == 9:
        erg = enigma_brute_force.getText(text, passPhrase, steckerbrett)

    return erg
