import time

def entero(variableint, string1):
    while True:
        try:
            variableint = int(input(string1))
            return variableint
        except:
            print("ERROR! No es un número entero!")
            time.sleep(1)

def cantidad(cantidad, variableint, listanombre, listacantidad):
    # Insersion de la cantidad
    while True:
        cantidad = entero(cantidad, f"Ingresa la cantidad del producto: {listanombre[variableint-1]} que deseas llevar\n")

        if ((listacantidad[variableint-1]+cantidad)<0):
            print("Ingresa una cantidad valida!")
        else:
            listacantidad[variableint-1] += cantidad
            break