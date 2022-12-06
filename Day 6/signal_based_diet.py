from collections import Counter
input = open("input.txt").read().strip()


# Za i od 0 do 4095
tekac = 0

for x in input:
    temp = input[tekac:tekac+4 ]
    freq = Counter(temp)
    if len(temp) == len(freq):
        break
    else:
        tekac += 1

print("Part one solution:",tekac +4)

tekac = 0

for x in input:
    temp = input[tekac:tekac+14 ]
    freq = Counter(temp)
    if len(temp) == len(freq):
        break
    else:
        tekac += 1

print("Part two solution:",tekac+14)