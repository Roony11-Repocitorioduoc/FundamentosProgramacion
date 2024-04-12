# Menu de comandos en cmd

import os
import time

while True:
    os.system("cls")

    print(f'''
    Menu Principal
    1. ipconfig
    2. hola mundo
    3. salir

    ''')

    cPrincipal=str(input("\nIngresa tu opcion\n"))

    if ((cPrincipal=="1") or (cPrincipal=="2") or (cPrincipal=="3")):
        if (cPrincipal=="1"):
            os.system("cls")

            os.system("ipconfig")
            time.sleep(5)
        elif (cPrincipal=="2"):
            print("Hola mundo!")

            time.sleep(5)
        elif (cPrincipal=="3"):
            print("Saliendo...")
            time.sleep(5)
            break
    else:
        print("Ingresa una opcion valida!")
        time.sleep(3)