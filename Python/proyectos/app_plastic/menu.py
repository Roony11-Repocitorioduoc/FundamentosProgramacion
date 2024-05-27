import os

def mostrar(lista, string1, string2):
    os.system("cls")
    print(string1)
    for i in range(len(lista)):
        print(f"{i+1}.- {lista[i]}")
    if (string2=="SI"):
        print(f"0.- Salir\n")

def boleta():
    print()