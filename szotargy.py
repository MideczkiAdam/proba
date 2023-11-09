li = []

while True:
    sorszam = 1
    szerzo = input("A könyv szerzője: ")
    if szerzo == "":
        break
    cim = input("A könyv címe: ")
    li.append({
        "Szerző" : szerzo,
        "cím" : cim
    }
    )
    sorszam += 1
print(li)
