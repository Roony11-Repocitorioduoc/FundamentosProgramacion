import os
import time

def entero(titulo):
    while True:
        try:
            variableentera = int(input(titulo))
            return variableentera
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)
        
def cambio(atributo, atributos, seleccion):
    atributos[atributo[seleccion-1]] = input(f"Ingresa el atributo: {atributo[seleccion-1]} a cambiar\n").lower().strip()
    