tarolo = [["O","O","O"],["O","O","O"],["O","O","O"]]
def drawboard():
    for o in range(3):
        for s in range(3):
            print(tarolo[o][s], end="")
        print("")

while True:
    osz = int(input("Oszlop: "))
    sor = int(input("Sor: "))
    if osz > 2:
        print("Vége!")
        break
    if osz < 0:
        print("Vége!")
        break
    if sor > 2:
        print("Vége!")
        break
    if sor < 0:
        print("Vége!")
        break
    tarolo[osz][sor] = "+"
    drawboard()