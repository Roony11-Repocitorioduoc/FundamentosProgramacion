import time
import os
import validar
    
def mostrar(lista):
    variableint = 0
    os.system("cls")
    for item in range(len(lista)):
        print(f"{item+1}.- {lista[item]}")
    print(f"0.- Salir\n")
    
    while True:
        variableint = validar.entero(variableint, f"Ingresa tu opción (0 - {len(lista)})\n")

        if (0<=variableint<=len(lista)):
            return variableint
        else:
            print("Ingresa un valor dentro de los rangos del menú")
            time.sleep(1)
    