import time
import os

my_list = ["Menu principal", "Menu Secundario", "Menu Terciario"]
my_listp = ["Sumar"]
my_lists = ["Saludar"]
my_listt = ["Preguntar edad"]

def espera_tecla():
    input("Preciona ENTER para continuar")

def mostrar_menu(nombres):
    os.system("cls")
    print("Menú:")
    for i, nombre in enumerate(nombres, start=1):
        print(f"{i}.- {nombre}")
    print("\n0.- Salir")

def accion_menu1():
    while True:
        id = input("Ingresa opción: \n")
        if (id=="0"):
            print("Saliendo...")
            time.sleep(3)
            break
        elif (id.isdigit()):
            opcion = int(id)
            if (1 <= opcion <= len(my_listp)):
                if (opcion==1):
                    numero1 = float(input("Ingresa número 1:\n"))
                    numero2 = float(input("Ingresa número 2:\n"))

                    print(f"La suma de {numero1} + {numero2} es {numero1+numero2}")
            else:
                print("Selecciona una opción valida!")
                espera_tecla()
        else:
            print("Por favor, ingresa un número!")
            espera_tecla()

def accion_menu2():
    while True:
        id = input("Ingresa opción: \n")
        if (id=="0"):
            print("Saliendo...")
            time.sleep(3)
            break
        elif (id.isdigit()):
            opcion = int(id)
            if (1 <= opcion <= len(my_lists)):
                if (opcion==1):
                    nombre=input("Ingresa tu nombre:\n")
                    print(f"Saludos {nombre}")
                else:
                    print("Selecciona una opción valida!")
                    espera_tecla()
            else:
                print("Por favor, ingresa un número!")
                espera_tecla()

def accion_menu3():
    while True:
        id = input("Ingresa opción: \n")
        if (id=="0"):
            print("Saliendo...")
            time.sleep(3)
            break
        elif (id.isdigit()):
            opcion = int(id)
            if (1 <= opcion <= len(my_listt)):
                if (opcion==1):
                    edad=float(input("Ingresa tu edad:\n"))
                    print(f"Tu edad es: {edad}")
            else:
                print("Selecciona una opción valida!")
                espera_tecla()
        else:
            print("Por favor, ingresa un número!")
            espera_tecla()

def accion_menup(id):
    if (id==1):
        os.system("cls")
        print("Menu Principal\n")

        mostrar_menu(my_listp)
        accion_menu1()

        espera_tecla()
    elif (id==2):
        os.system("cls")
        print("Menu Secundario\n")

        mostrar_menu(my_lists)
        accion_menu2()

        espera_tecla()
    elif (id==3):
        os.system("cls")
        print("Menu Terciario\n")

        mostrar_menu(my_listt)
        accion_menu3()

        espera_tecla()

while True:
    mostrar_menu(my_list)
    id = input("Ingresa opción: \n")

    if (id=="0"):
        print("Saliendo...")
        time.sleep(3)
        break
    elif (id.isdigit()):
        opcion = int(id)
        if (1 <= opcion <= len(my_list)):
            print(f"Seleccionaste: {my_list[opcion-1]}")
            accion_menup(opcion)
        else:
            print("Selecciona una opción valida!")
            espera_tecla()

    else:
        print("Por favor, ingresa un número!")
        espera_tecla()
