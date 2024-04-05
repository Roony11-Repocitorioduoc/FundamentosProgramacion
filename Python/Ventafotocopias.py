import time

mensaje_error="Ingresa una opción valida!\n"
valorFotocopia=20
totalRecaudado=0
totalFotocopias=0
totalVentas=0

def volver_menu(tiempo):
    print(f"Espera {tiempo} segundos!")
    time.sleep(tiempo)

while True:
    print("-Menu Principal-\n1. Venta fotocopias\n2. Estadisticas\n3. Salir\n")

    cPrincipal=input("Ingresa tu opción\n")

    if ((cPrincipal=="1") or (cPrincipal=="2") or (cPrincipal=="3")):
        if (cPrincipal=="1"):
            print("Menu Venta")

            while True:
                cantidadFotocopias=int(input(f"Cuantas fotocopias quieres? (Valor ${valorFotocopia} (c/u), descuento de 10% al llevar más de 30!)\n"))
                if (cantidadFotocopias<=0):
                    print(f"{mensaje_error}")
                    time.sleep(1)
                else:
                    break
            
            print(f"Ticket de venta\nCantidad de fotocopias: {cantidadFotocopias}")

            totalFotocopias=totalFotocopias+cantidadFotocopias

            if (cantidadFotocopias>30):
                print(f"Total: {cantidadFotocopias*valorFotocopia}\nDescuento: {cantidadFotocopias*valorFotocopia*0.1}\nTotal a pagar: {cantidadFotocopias*valorFotocopia*0.9}")
                totalRecaudado=totalRecaudado+cantidadFotocopias*valorFotocopia*0.9
            else:
                print(f"Total a pagar: {cantidadFotocopias*valorFotocopia}")
                totalRecaudado=totalRecaudado+cantidadFotocopias*valorFotocopia
            
            totalVentas+=1

            volver_menu(4)
        elif (cPrincipal=="2"):
            print("Menu Estadisticas")

            if (totalVentas<=0):
               print(f"No hay ventas")
            else:
                print(f"Cantidad de ventas: {totalVentas}\nCantidad de fotocopias: {cantidadFotocopias}, Promedio de fotocopias por venta: {cantidadFotocopias/totalVentas}\nTotal recaudado: ${totalRecaudado}, Promedio recaudado por venta: ${totalRecaudado/totalVentas}")

            volver_menu(4)
        elif(cPrincipal=="3"):
            print("Saliendo...")
            time.sleep(2)
            break
    else:
        print(f"{mensaje_error}")
        time.sleep(1)
