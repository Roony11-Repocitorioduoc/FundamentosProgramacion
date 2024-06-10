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
        
def cambio(atributo, )
    