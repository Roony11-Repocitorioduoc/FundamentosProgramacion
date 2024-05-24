import time
import os
    
def mostrar(variableint, lista):
    os.system("cls")
    for item in range(len(lista)):
        print(f"{item+1}.- {lista[item]}")
    print(f"0.- Salir\n")
    
    while True:
        try:
            variableint = int(input(f"Ingresa tu opción (0 - {len(lista)})\n"))
            if (0<=variableint<=len(lista)):
                return variableint
                break
            else:
                print("Ingresa un valor dentro de los rangos del menú")
                time.sleep(1)
        except:
            print("Ingresa un número entero!")
            time.sleep(1)
    