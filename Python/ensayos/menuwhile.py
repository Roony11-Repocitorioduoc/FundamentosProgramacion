import time

while True:
    print("Selecciona una opción\n1. Menu Hola\n2. Menu Saludos\n3. Menu Salir")
    cPrincipal=input("Ingresa tu opción: ")

    if ((cPrincipal=="1") or (cPrincipal=="2") or (cPrincipal=="3")):
        if (cPrincipal=="1"):
            print("Menu Hola\n Holaaaaaaa")
            print("\n Espera un momento")
            time.sleep(2)
        elif (cPrincipal=="2"):
            print("Menu Saludo\n Saludoooooos")
            print("\n Espera un momento")
            time.sleep(2)
        elif (cPrincipal=="3"):
            print("Saliendo...")
            time.sleep(1)
            break
    else:
        print("Ingresa una opción valida!")