podatki = open("input.txt").read().strip().split("\n")


part_one_result = 0
part_two_result = 0
for x in podatki:
    x = x.split(",")
    x1 = x[0].split("-")
    x11 = int(x1[0])
    x12 = int(x1[1])

    x2 = x[1].split("-")
    x21 = int(x2[0])
    x22 = int(x2[1])


    set1 = set(range(x11,x12+1))
    set2 = set(range(x21,x22+1))

    if set1 <= set2:
        part_one_result += 1
    elif set2 <= set1:
        part_one_result += 1

    if len(set1&set2) != 0:
        part_two_result += 1

print(part_one_result,"sets are subsets of other sets.")
print(part_two_result,"sets have something in common.")