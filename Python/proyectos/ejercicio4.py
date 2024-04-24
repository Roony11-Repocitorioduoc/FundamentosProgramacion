import os
import time

menu_principal = ["Iniciar Sesión", "Registrar Usuario"]
menu_usuario = ["Realizar Llamada", "Enviar Correo Electrónico"]
menu_llamada = ["Llamar Número", "Registrar Número"]

usuarios = []
claves = []

numeros = []

mensaje_numero = "Ingresa un número entero!"
mensaje_outindex = "Ingresa un número entero dentro del rango!"

def mostrar_menu(menu): # ingresa lista a mostrar
    for opc in range(len(menu)):
        print(f"{opc+1}. {menu[opc]}")
    print(f"0. Salir")
    
def textotiempo(tiempo, texto):
    print(texto)
    time.sleep(tiempo)

def login(listau, listac): # listau: lista usuarios, listac: lista claves
    while True:
        os.system("cls")
        loginUsuario = input("Ingresa tu usuario\n")

        if (loginUsuario in listau):
            loginClave = input("Ingresa tu clave\n")
            if(loginClave in listac):
                os.system("cls")
                break
            else:
                textotiempo(1, "Contraseña incorrecta!")
                #print("Contraseña incorrecta!")
                #time.sleep(1)
        else:
            textotiempo(1, "No existe el usuario!")
            #print("No existe el usuario!")
            #time.sleep(1)

def seleccion_menu(lista, opc):
    if (opc.isdigit()):
        opc = int(opc)
        if (0<= opc<= len(lista)):
            return opc
        else:
            textotiempo(1, mensaje_outindex)
            #print(mensaje_outindex)
            #time.sleep(1)
    else:
        textotiempo(1, mensaje_numero)
        #print(mensaje_numero)
        #time.sleep(1)

def registrar_usuario(nombre, clave):
    usuarios.append(nombre)
    claves.append(clave)
    print(f"Usuario: {nombre} creado satisfactoriamente")
    time.sleep(1)

def main_llamada():
    while True:
        os.system("cls")
        mostrar_menu(menu_llamada)
    
        opcllamada = input("\nIngresa tu opción:\n")
    
        opcion_llamada = seleccion_menu(menu_llamada, opcllamada)
    
        if (opcion_llamada==0):
            break
        elif (opcion_llamada==1):
            if (len(numeros)==0):
                textotiempo(1, "Debe de haber almenos un número registrado en el sistema")
            else:
                mostrar_menu(numeros)
                opcnumero = input("\nIngresa tu opción:\n")
            
                opcion_numero = seleccion_menu(numeros, opcnumero)
            
                print(f"Llamando a: +56{numeros[opcion_numero]}")
        elif (opcion_llamada==2):
            while True:
                os.system("cls")
                registro_numero = input("Ingresa el número para registrar\nRequisitos\n-Debe ingresar 9 digitos\n-Debe comenzar por un 9 o un 2\n")
                totaln=0
        
                for n in registro_numero:
                    totaln+=1
        
                if (totaln==9):
                    textotiempo(2, f"Número: +56{registro_numero} satisfactoriamente guardado")
                    break
                else:
                    textotiempo(1, "Ingresa un número de un total de 9 digitos")
            
            
def main_usuario():
    while True:
        os.system("cls")
        mostrar_menu(menu_usuario)

        preopcu = input("\nIngresa tu opción:\n")

        opcion_elegidau = seleccion_menu(menu_usuario, preopcu)

        if (opcion_elegidau==0):
            break
        elif (opcion_elegidau==1):
                main_llamada()
        elif (opcion_elegidau==2):
            print("Menu correo") 
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
                textotiempo(1, "Primero debes tener almenos registrado un usuario!")
                #print("Primero debes tener almenos registrado un usuario!")
                #time.sleep(1)
            else:
                login(usuarios, claves)
                
                main_usuario()            
        elif(opcion_elegida==2):
                while True:
                    os.system("cls")
                    nusuario = input("Ingresa el nombre del usuario:\n")
                    if (nusuario in usuarios):
                        textotiempo(1, "Este usuario ya esta registrado!")
                        #print("Este usuario ya esta registrado!")
                        #time.sleep(1)
                    else:
                        break
                nclave = input("Ingresa la clave de tu usuario\n")

                registrar_usuario(nusuario, nclave)

main()




