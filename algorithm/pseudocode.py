kalrtext = "Ich bin ein Klartext"
schlüssel = 3
geheimtext = ""


schlüssel = round(schlüssel)
text = ensureSideCondition(klartext, schlüssel)
length = len(klartext)

für x bis schlüssel
    für y von x bis length in schlüssel schritten
        geheimtext += text[y]

print(geheimtext)
