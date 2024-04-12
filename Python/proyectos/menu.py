import os
import time

# Funcion espera tecla para continuar
def esperar_tecla(segundos):
    time.sleep(segundos)
    input("\nPresiona ENTER para continuar")

m_principal = ["Ingresar usuario", "Ver Usuarios"]
lista_usuario = ["Nombre", "Edad"]

m_usuario = []

# Segun esta logica debo definirlo afuera! con la lista de atributos.
n_columnas = len(lista_usuario)

def mostrar_menu(lista):
    for i, articulo in enumerate(lista, start=1):
        print(f"{i}.- {articulo}.")
    print("\n0.- Salir.")

def seleccion_menu(opcion, lista):
    if (opcion=="0"):
        print("Saliendo...")
        return 0
    elif (opcion.isdigit()):
        opcint = int(opcion)
        if (1 <= opcint <= len(lista)):
            return opcint
        else:
                print("Ingresa una opción valida!")
                time.sleep(2)
    else:
        print("Ingresa un número")
        time.sleep(2)

def ingresar_usuario(matriz, lista_atributos, n_columna):
    nueva_fila=[]

    for columna in range(n_columna):
        if (len(matriz)==0):
            nueva_fila.append(lista_atributos[columna])
        else:
            nueva_fila.append(input(f"\nIngrese su {lista_atributos[columna].lower()}\n"))

    matriz.append(nueva_fila)
    
    # Probemos la matriz
    #if(len(matriz_datos)>1):
    #    for fila in matriz_datos:
    #        print(fila)

def mostrar_usuario(matriz):
        for fila in matriz:
            print(fila)

def menu_principal():
    while True:
        os.system("cls")
        mostrar_menu(m_principal)

        opc = input("Ingresa la opción del menú: \n")

        opcion_elegida = seleccion_menu(opc, m_principal)

        if (opcion_elegida==0):
            break
        elif (opcion_elegida==1):
            os.system("cls")
            print("Ingresar usuario")
            ingresar_usuario(m_usuario, lista_usuario, n_columnas)

            esperar_tecla(1)
        elif (opcion_elegida==2):
            os.system("cls")
            print("Ver usuario")
            mostrar_usuario(m_usuario)

            esperar_tecla(1)
    
def main():
        menu_principal()

if __name__ == "__main__":
    main()


