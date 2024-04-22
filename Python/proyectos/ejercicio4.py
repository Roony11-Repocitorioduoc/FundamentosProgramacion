import os
import time

menu_principal = ["Iniciar Sesión", "Registrar Usuario"]
menu_usuario = ["Realizar Llamada", "Enviar Correo Electrónico"]

usuarios = []
claves = []

mensaje_numero = "Ingresa un número entero!"
mensaje_outindex = "Ingresa un número entero dentro del rango!"

def mostrar_menu(menu): # ingresa lista a mostrar
    for opc in range(len(menu)):
        print(f"{opc+1}. {menu[opc]}")
    print(f"0. Salir")

def seleccion_menu(lista, opc):
    if (opc.isdigit()):
        opc = int(opc)
        if (0<= opc<= len(lista)):
            return opc
        else:
            print(mensaje_outindex)
            time.sleep(1)
    else:
        print(mensaje_numero)
        time.sleep(1)

def registrar_usuario(nombre, clave):
    usuarios.append(nombre)
    claves.append(clave)
    print(f"Usuario: {nombre} creado satisfactoriamente")
    time.sleep(1)

def main():
    while True:
        os.system("cls")
        mostrar_menu(menu_principal)

        preopc = input("\nIngresa tu opción:\n")

        opcion_elegida = seleccion_menu(menu_principal, preopc)

        if (opcion_elegida==0):
            break
        elif (opcion_elegida==1):
            os.system("cls")
            if (len(usuarios)==0):
                print("Primero debes tener almenos registrado un usuario!")
                time.sleep(1)
            else:
                while True:
                    os.system("cls")
                    loginUsuario = input("Ingresa tu usuario\n")

                    if (loginUsuario in usuarios):
                        loginClave = input("Ingresa tu clave\n")
                        if(loginClave in claves):
                            os.system("cls")
                            break
                        else:
                            print("Contraseña incorrecta!")
                            time.sleep(1)
                    else:
                        print("No existe el usuario!")
                        time.sleep(1)
                
                while True:
                    os.system("cls")
                    mostrar_menu(menu_usuario)

                    preopcu = input("\nIngresa tu opción:\n")

                    opcion_elegidau = seleccion_menu(menu_usuario, preopcu)

                    if (opcion_elegidau==0):
                        break
                    elif (opcion_elegidau==1):
                        print("Menu llamada")
                        time.sleep(1)
                    elif (opcion_elegidau==2):
                        print("Menu correo") 
                        time.sleep(1)             
        elif(opcion_elegida==2):
                while True:
                    os.system("cls")
                    nusuario = input("Ingresa el nombre del usuario:\n")
                    if (nusuario in usuarios):
                        print("Este usuario ya esta registrado!")
                        time.sleep(2)
                    else:
                        break
                nclave = input("Ingresa la clave de tu usuario\n")

                registrar_usuario(nusuario, nclave)

main()




