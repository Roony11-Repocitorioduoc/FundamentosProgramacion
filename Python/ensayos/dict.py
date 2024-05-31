import os
import time

# Definamos nuestro diccionario vacío
dict = {}

# Definamos nuestra lista vacía
lista = []

# Datos de nuestro diccionario
nombre = ""
edad = 0
carrera = ""
# Menú
control = 0

while True:
    os.system("cls")
    print(f"Menú ingreso\n1. Ingresar usuario\n2. Mostrar la lista\n3. Salir\n")
    
    control = int(input(f"Ingresa tu opción\n"))
    
    if control==1:
        nombre = input(f"Ingresa el nombre\n")
        edad = int(input(f"Ingresa la edad\n"))
        carrera = input(f"Ingresa la carrera\n")
        
        dict = {
            "Nombre" : nombre,
            "Edad" : edad,
            "Carrera" : carrera
        }
        
        lista.append(dict)
    elif control==2:
        os.system("cls")
        # Mostrar cada indice de la lista como fila
        #for fila in lista:
        #    print(fila)
        
        for i in range(len(lista)):
            for k, v in lista[i].items():
                print(f"{k} - {v}")
            if (i<len(lista)-1):
                print("---")
        
        
        input(f"\nENTER\n")
    elif control==3:
        break


