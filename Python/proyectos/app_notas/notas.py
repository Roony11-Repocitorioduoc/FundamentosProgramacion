import os
import time
import validar

# Carga notas a una "lista"
def cargar(lista):
    cantidad = 0
    nota = 0.0
    
    if (len(lista)!=0):
        print(F"Esto borrara los datos anteriores!")
        time.sleep(1)
        lista.clear()


    while True:
        os.system("cls")
        cantidad = validar.entero(cantidad, f"Ingresa la cantidad de notas!\n")

        if (cantidad<=1):
            print(f"Debes ingresar más de una nota!\n")
        else:
            break
    
    for item in range(cantidad):
        while True:
            nota = validar.decimal(nota, f"Ingresa la nota {item+1}\n")

            if (1<=nota<=7):
                break
            else:
                print(f"Ingresa una nota en un intervalo [1, 7]")
        
        lista.append(nota)

def promedio(lista):
    promedio = 0.0
    if (len(lista)>1):
        promedio = sum(lista)/len(lista)

        os.system("cls")
        print(f"El promedio es {promedio}")
    else:
        print("No hay suficiente notas!")
    
    