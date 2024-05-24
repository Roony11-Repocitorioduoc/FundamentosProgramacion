import os
import time

#optimizados para notas
# Carga un int en una variable con dos strings
def cargar_int(variableint, string1, string2):
    while True:
        try:
            variableint = int(input(string1))
            if (1<variableint):
                return variableint
                break
            else:
                print(string2)
                time.sleep(1)
        except:
            print("Ingresa un número!")
            time.sleep(1)

# Carga un float en una variable con dos strings
def cargar_float(variablefloat, string1, string2):
    while True:
        try:
            variablefloat = float(input(string1))
            if (1<=variablefloat<=7):
                return variablefloat
                break
            else:
                print(string2)
                time.sleep(1)
        except:
            print("Ingresa un número!")
            time.sleep(1)

# Carga notas a una "lista"
def cargar(lista):
    cantidad = 0
    nota = 0.0
    
    cantidad = cargar_int(cantidad, f"Ingresa la cantidad de notas!\n", "Debe haber más de 1 nota!")
    
    for item in range(cantidad):
        nota = cargar_float(nota, f"Ingresa la nota {item+1}\n", "Ingresa un valor de nota valido!")
        
        lista.append(nota)

def promedio(lista):
    promedio = 0.0
    if (len(lista)>1):
        promedio = sum(lista)/len(lista)
    
        print(f"El promedio es {promedio}")
    else:
        print("No hay suficiente notas!")
    
    