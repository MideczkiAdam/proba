'''
Az adatok beolvasása fájlból,
egy-egy sor az 'adatok' nevű lista egy-egy eleme
'''
adatok = []
with open('autok_listaja.txt', 'r', encoding='utf-8') as fajl:
    for sor in fajl:
        # strip() metódus eltávolítja a sorvégi \n-t
        adatok.append(sor.strip())


'''
A 'autok' nevű lista 'auto' nevű szótár típusokat fog tartalmazni,
egy autó adatait egy szótár tárolja
'''
auto = {}  # egy auto adatai
autok = []  # szótárakat tartalmazó lista
for elem in adatok:
    auto_adatai = elem.split()
    auto['rendszam'] = auto_adatai[0]
    auto['marka'] = auto_adatai[1]
    auto['tipus'] = auto_adatai[2]
    auto['kor'] = int(auto_adatai[3])
    if auto_adatai[4] == '1':
        auto['javitva'] = True
    else:
        auto['javitva'] = False
    auto['koltseg'] = int(auto_adatai[5])

    autok.append(auto)
    auto = {}  # egy új, üres szótár objektum deklarálása ugyanazon a néven

#1

legor = autok[0]
for auto in autok:
    if auto["kor"] > legor["kor"]:
        legor = auto
print(f"A legöregebb autó egy {legor["marka"]} {legor["tipus"]}, ami {legor["kor"]} éves")

#2

for auto in autok:
    if auto["javitva"]:
        print(auto["rendszam"])

#3

összeg = 0
for auto in autok:
    összeg += auto["koltseg"]
print(f"Átlagos javítási költség: {összeg / len(autok)}")

#4

keresett = None
sajat = input("Rendszám: ")
for auto in autok:
    if auto["rendszam"] == sajat:
        keresett = auto
if keresett != None:
    print("Műhelyben van")
else:
    print("Nincs a műhelyben")

#5

betu = input("Betű: ")
for auto in autok:
    if betu.upper() in auto["marka"].upper() or betu.upper() in auto["tipus"].upper():
        print(f"{auto["marka"]} {auto["tipus"]}")