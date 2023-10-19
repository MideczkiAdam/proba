import random
tarolo = [[],[],[],[],[]]
poz = [[],[],[],[],[]]
for i in range(3):
    tarolo[0].append(random.randint(-5,5))
    tarolo[1].append(random.randint(-5,5))
    tarolo[2].append(random.randint(-5,5))
    tarolo[3].append(random.randint(-5,5))
    tarolo[4].append(random.randint(-5,5))

for i in range(3):
    if tarolo[0][i] > 0:
        poz[0].append(tarolo[0][i])
for i in range(3):
    if tarolo[1][i] > 0:
        poz[1].append(tarolo[1][i])
for i in range(3):
    if tarolo[2][i] > 0:
        poz[2].append(tarolo[2][i])
for i in range(3):
    if tarolo[3][i] > 0:
        poz[3].append(tarolo[3][i])
for i in range(3):
    if tarolo[4][i] > 0:
        poz[4].append(tarolo[4][i])

print(tarolo)
print(poz)
