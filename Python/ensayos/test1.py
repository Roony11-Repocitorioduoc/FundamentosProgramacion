import os
import time

# Funcion espera tecla para continuar
def esperar_tecla(segundos):
    time.sleep(segundos)
    input("\nPresiona ENTER para continuar")

lista = ["Item", "Nombre", "Edad"]
principal = ["Ingresar usuario", "Mostrar datos"]

n_columnas = len(lista)

matriz = []

# Funcion mostrar matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
    
    esperar_tecla(1)

# Funcion de ingreso de usuario
def ingresar_usuario():
    while True:
        nueva_fila=[]

        for columna in range(n_columnas):
            if (len(matriz)==0):
                nueva_fila.append(lista[columna])
            else:
                nueva_fila.append(input(f"Ingrese su {lista[columna].lower()}"))

        matriz.append(nueva_fila)
        break
        '''continuar = input("Deseas agregar datos? (s para continuar)")
        
        if (continuar.lower()!="s"):
            break
            print("Volviendo...")
            esperar_tecla(1)
        
        nueva_fila = [] # Matriz fila vacia como placeholder
        for columna in range(n_columnas):
            if (len(matriz)==0): # Crea los titulos de la tabla
                nueva_fila.append(lista[columna]) 
            else: # Toda fila despues de los titulos
                if (columna>=1): # Nombre, edad
                    nueva_fila.append(input(f"\nIngresa tu {lista[columna].lower()}\n"))
                else: # Numero del item (No funciona, a priori)
                    nueva_fila.append(columna)
                
        # Ingresa la fila de datos a la matriz
        matriz.append(nueva_fila) '''


# Funcion muestra un menu a partir de los items de una lista
def mostrar_menu(lista):
    for i, opcion in enumerate(lista, start=1): #Enumera los datos de la lista menu y les asigna un numero parte en el 1
        print(f"{i}.- {opcion}") # Crea el menu
    print("\n0.- Salir.") # 0 Salir
    
# Logica menu principal
def logic_principal():
    while True:
        os.system("cls")
        mostrar_menu(principal)
        opcion = input("Ingresa tu opción.\n")
        if (opcion=="0"):
            print("Saliendo...")
            break
        elif (opcion.isdigit()):
            opcint = int(opcion)
            if (1 <= opcint <= len(principal)):
                if (opcint==1):
                    os.system("cls")
                    ingresar_usuario()
                elif (opcint==2):
                    # Mostrar la matriz cuando tenga datos!
                    os.system("cls")
                    if (len(matriz)!=0):
                        mostrar_matriz(matriz)
                    else:
                        print("Primero debes ingresar datos a la matriz.")
                        esperar_tecla(1)
            else:
                print("Ingresa una opción valida!")
                esperar_tecla(1)
        else:
            print("Ingresa un número")
            esperar_tecla(1)
            
logic_principal()
    
    



