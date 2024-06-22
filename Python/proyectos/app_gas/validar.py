import os
import time


def entero(titulo):
    """Ingresa un entero y valida si es asi
    """
    while True:
        try:
            variableentera = int(input(titulo))
            return variableentera
        except Exception as e:
            print("Error:", e)
            os.system("pause")
            continue