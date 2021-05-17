from algorithm import caesar_cipher


def control(encryption_id, text, shift):

    options = {
        0: caesar_cipher.encrypt(text, shift),
        1: caesar_cipher.decrypt(text, shift)
    }

    return options[int(encryption_id)]
