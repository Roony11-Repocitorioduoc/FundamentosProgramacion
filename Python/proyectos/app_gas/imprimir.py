import os


def menu(lista, titulo, bool):
    """Imprime un menu desde una lista
    """
    os.system("cls")
    print(titulo)
    for i in range(len(lista)):
        print(f"{i+1}.- {lista[i]}")
    if bool:
        print(f"{len(lista)+1}.- Salir")