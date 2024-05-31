import os
import time

control_menu = 0

def crear(titulo, lista_opciones, mostrar_salir):
    os.system("cls")
    print(f"{titulo}\n")
    for i in range(len(lista_opciones)):
        print(f"{i+1}.- {lista_opciones[i]}")
    print(" ")
    if mostrar_salir==1:
        print("0.- Salir\n")

def matriz(matriz):
    for fila in matriz:
        print(fila)
    print(" ")
