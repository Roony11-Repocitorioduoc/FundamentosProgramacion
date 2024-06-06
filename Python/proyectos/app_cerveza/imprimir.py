import os

def menu(lista_menu):
    os.system("cls")
    for i in range(len(lista_menu)):
        print(f"{i+1}.- {lista_menu[i]}")