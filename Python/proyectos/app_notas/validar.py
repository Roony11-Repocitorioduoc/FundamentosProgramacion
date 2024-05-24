import time

def entero(variableint, string1):
    while True:
        try:
            variableint = int(input(string1))
            return variableint
        except:
            print("Ingresa un número!")
            time.sleep(1)

# Carga un float en una variable con un string
def decimal(variablefloat, string1):
    while True:
        try:
            variablefloat = float(input(string1))
            return variablefloat
        except:
            print("Ingresa un número decimal!")
            time.sleep(1)