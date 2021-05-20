
def skytale_encrypt(text, umfang):
    umfang = round(umfang)
    text = ensureSideCondition(text, umfang)
    length = len(text)
    cipher = ""
    for x in range(0, umfang):
        for y in range(x, length, umfang):
            cipher += text[y]

    return cipher


def ensureSideCondition(text, umfang):
    umfang = round(umfang)
    length = len(text)
    remainder = length % umfang
    while remainder != 0:
        text += " "
        length = len(text)
        remainder = length % umfang

    return text


def skytale_decrypt(text, umfang):
    umfang = round(umfang)
    length = len(text)
    umfang = length/umfang
    plaintext = skytale_encrypt(text, umfang)

    return plaintext


if __name__ == '__main__':
    print(skytale_decrypt("Mein Name ist Noah", 4))
