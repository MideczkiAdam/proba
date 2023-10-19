import pprint

age = int(input("Age: "))
name = input("Name: ")
breed = input("Breed: ")
okmany = input("Okmány: ")

dog ={
    "age": age,
    "name": name,
    "breed": breed,
    "okmany": okmany 
}
print(dog)
macs ={
    "name": "Ati",
    "age": 69
}
ask = input("Akarsz változtatni?")
if ask == "Igen":
    asd = input("Melyiket?")
    if asd == "Nevét":
        nev = input("Név: ")
        macs["name"] = nev
        print(macs)
    if asd == "Korát":
        kor = int(input("Kor: "))
        macs["age"] = kor
        print(macs)
else:
    print(macs)

koc = {
    "name": "Apu",
    "age": 14,
    "okmany": True
}
while True:
    a = input("Akarsz még hozzáadni?")
    if a == "igen":
        mit = input("Mit?")
        mire = input("mire?")
        koc[mit] = mire
        print(koc)
    if a == "nem":
        print(koc)
        break

import random

vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "	Hanna" ]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér" ]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]
osztaly = ["A","B","C","D"]

res = []

for i in range(8):
    res.append({
    "név": vezeteknevek[random.randrange(len(vezeteknevek))] + " " + keresztnevek[random.randrange(len(keresztnevek))],
    "életkor": random.randint(14,19),
    "évfolyam": random.randint(9,12),
    "osztály": osztaly[random.randrange(len(osztaly))],
    "cím": {
        "település": telepulesek[random.randrange(len(telepulesek))],
        "utca": utcak[random.randrange(len(utcak))],
        "házszám": random.randint(1,50)
    }
    })

pprint.pprint(res)