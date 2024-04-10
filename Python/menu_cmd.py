# Menu de comandos en cmd

import os
import time

print(f'''
Menu Principal
1. ipconfig
2. hola mundo

''')

while True:
    cPrincipal=str(input("\nIngresa tu opcion\n"))

    if ((cPrincipal=="1") or (cPrincipal=="2")):
        if (cPrincipal=="1"):
            os.system("cls")

            os.system("ipconfig")
            time.sleep(5)
            break
        if (cPrincipal=="2"):
            print("Hola mundo!")

            time.sleep(5)
            break
    else:
        print("Ingresa una opcion valida!")