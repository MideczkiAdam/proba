# fájl tartalmának kiírása
def showtodos():
    fajl = open("todo.txt","r", encoding="utf-8")

    sorok = fajl.readlines()
    fajl.close

    for sor in sorok:
        print(sor.strip())

#Írás a fájlba
def writetodos(todo):
    irosfajl = open("todo.txt","a", encoding="utf-8")
    irosfajl.write(todo + "\n")
    irosfajl.close

#Törlés index szerint
def deletetodos():
    file = open("todo.txt","r", encoding="utf-8")
    sorok = file.readlines()
    file.close
    for i in range(len(sorok)):
        print(i, sorok[i].strip())
    
    index = int(input("Törlendő: "))
    file = open("todo.txt", "w", encoding="utf-8")

    for i in range(len(sorok)):
        if i != index:
            file.write(sorok[i])
    file.close

deletetodos()

# while True:
#     input_sor = input("Új: ")
#     if input_sor != "X":
#         irosfajl.write(input_sor + "\n")
#     else:
#         break