import pprint

podatki = open("input.txt").read().strip().split("\n")


box = {
    1: [["Z"],["T"],["F"],["R"],["W"],["J"],["G"]],
    2: [["G"],["W"],["M"]],
    3: [["J"],["N"],["H"],["G"]],
    4: [["J"],["R"],["C"],["N"],["W"]],
    5: [["W"],["F"],["S"],["B"],["G"],["Q"],["V"],["M"]],
    6: [["S"],["R"],["T"],["D"],["V"],["W"],["C"]],
    7: [["H"],["B"],["N"],["C"],["D"],["Z"],["G"],["V"]],
    8: [["S"],["J"],["N"],["M"],["G"],["C"]],
    9: [["G"],["P"],["N"],["W"],["C"],["J"],["D"],["L"]]
}


def line_splitter(line):
    line = line.split(" ")
    amount,from_where,to_where = line[1],line[3],line[5]
    amount = int(amount)
    from_where = int(from_where)
    to_where = int(to_where)
    return (amount,from_where,to_where)

"""
Part one:
Since pop both removes and returns the value, we simply pop off the value of an item
and pop in on another.

for x in podatki:
    temp = line_splitter(x)
    amount,from_where,to_where = temp
    for y in range(amount):
        box[to_where].append(box[from_where].pop(-1))
"""
# Pretty print: pprint.pprint(box)
# Anwser to part one: cwmtghbdw

for x in podatki:
    temp = line_splitter(x)
    amount,from_where,to_where = temp
    tempo = box[from_where][-amount:]
    for x in tempo:
        box[to_where].append(x)

    del box[from_where][-amount:]


pprint.pprint(box)
# Anwser to part two: sscgwjcrb