import string
from string import ascii_letters


podatki = open("input.txt")


abeceda_mala = list(string.ascii_lowercase)
abeceda_mala = dict(enumerate(abeceda_mala, start= 1))
abeceda_mala = dict([(value, key) for key, value in abeceda_mala.items()])


abeceda_vlka = list(string.ascii_uppercase)
abeceda_vlka = dict(enumerate(abeceda_vlka, start= 27))
abeceda_vlka = dict([(value, key) for key, value in abeceda_vlka.items()])

# Cuts a string in half then tells you what elements are in common.
def string_comparison(string):
    string1 = string[:len(string)//2]
    string2 = string[len(string) //2:]
    string1 = set(string1)
    string2 = set(string2)
    rez = string1 & string2
    for x in rez:
        rez = x

    return(rez)

data = podatki.read().split("\n")

result = 0
for x in podatki:
    y = x
    y = string_comparison(y)
    if y in abeceda_vlka:
        result += abeceda_vlka[y]
    elif y in abeceda_mala:
        result += abeceda_mala[y]

part_dos = 0
# i gre od 0 do dolžine niza, uzmae po tri
for i in range(0, len(data), 3):
    # za vsako trijico nizov pregelda če je znak u enem
    for char in data[i]:
        # in če je ta znak v drugem
        if char in data[i + 1]:
            # in je če je ta znak u tretjem
            if char in data[i + 2]:
                # vzame njegov index in doda 1
                # ascii letters šteje od 0 do 25 za male in  od 26 do 51 za vlke, dodamo 1
                part_dos += ascii_letters.index(char) + 1
                break
print(part_dos)

