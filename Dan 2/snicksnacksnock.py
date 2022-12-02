from unittest import case

podatki = open("input.txt")

data = podatki.read().split("\n")
sample = "A X"

def cases(case):
    score = 0
    match case:
        case "A X":
            score += 4
        case "A Y":
            score += 8
        case "A Z":
            score += 3

        case "B X":
            score += 1
        case "B Y":
            score += 5
        case "B Z":
            score += 9

        case "C X":
            score += 7
        case "C Y":
            score += 2
        case "C Z":
            score += 6

    return score

result_part_one = 0

for x in data:
    result_part_one += cases(x)

def case_switch(part_two):
    a = part_two
    match a:
        case "A X":
            a = "A Z"
        case "A Y":
            a = "A X"
        case "A Z":
            a = "A Y"

        case "B X":
            a = "B X"
        case "B Y":
            a = "B Y"
        case "B Z":
            a = "B Z"

        case "C X":
            a = "C Y"
        case "C Y":
            a = "C Z"
        case "C Z":
            a = "C X"

    return a

new_data = []
for z in data:
    temp = case_switch(z)
    new_data.append(temp)

print(data)
print(new_data)

result_part_two = 0
for y in new_data:
    result_part_two += cases(y)

print(result_part_two)