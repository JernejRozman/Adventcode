podatki = open("input.txt")

data = podatki.read().split("\n\n")

data = [[int(item) for item in pack.splitlines()] for pack in data]

data = sorted([sum(pack) for pack in data])


print(data[-1])
print(sum(data[-3:]))