import string

characters = list(map(chr, range(58, 127)))
print(characters)

print(ord("z"))

chr = 'a'
chr = ord(chr)
while True:
    if chr in range(ord('a'), ord('z')+1):
        print("Drine")
