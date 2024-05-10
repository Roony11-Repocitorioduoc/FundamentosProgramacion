import time
import os


# Vars
## Control de menú
control_principal = 0
control_venta = 0
control_codigo = 0
## Estadisticas
estadistica_ventas = 0 # cantidad de ventas
estadistica_galeria = 0 # cantidad de estradas del tipo vendidas
estadistica_vgaleria = 0 # recaudado de las entradas del tipo
estadistica_tribuna = 0
estadistica_vtribuna = 0
estadistica_cancha = 0
estadistica_vcancha = 0
estadistica_descuento = 0 # cantidad de descuentos realizados
## Strings menú
menu_principal = """--_ Menú Principal _--
1. Venta de entradas
2. Estadísticas
3. Salir
"""

menu_venta = f"""--_ Menú Venta
  |\tTipo\t|\tPrecio
1.|\tGalería\t|\t$20000
2.|\tTribuna\t|\t$35000
3.|\tCancha\t|\t$30000
"""

menu_codigo = f"""--_ Menú codigo descuento _--
¿Tienes codigo de descuento?
1. Si
2. No
"""

## Strings Mensaje usuarios
mensaje_outindex = "ERROR, Ingresa un número dentro de los rangos del menú!"
mensaje_valueerror = "ERROR, Ingresa un número entero!"
mensaje_enter = "Presiona ENTER para continuar"

while True:
    cantidad = 0 # cantidad de entradas
    entrada = "" # nombre de la entrada seleccionada
    stringdescuento = "" # string asociado al descuento para enseñar boleta
    descuento = 1 # descuento asociado a la entrada (1 sin descuento, 0.8 20% de descuento)
    precio = 0 # precio de la entrada seleccionada
    
    while True: # Validación menú principal
        os.system("cls")
    
        print (menu_principal)
        try:
            control_principal = int(input("Ingresa tu opción:\n"))
            if (1<=control_principal<=3):
                break
            else:
                print(mensaje_outindex)
                time.sleep(1)
        except:
            print(mensaje_valueerror)
            time.sleep(1)
            
    # Condicionales opciones de menú
    if (control_principal==1):
        
        while True: # Validación menú venta
            os.system("cls")
            print(menu_venta)
            
            try:
                control_venta = int(input("Ingresa tu opción:\n"))
                if (1<=control_venta<=3):
                    break
                else:
                    print(mensaje_outindex)
                    time.sleep(1)
            except:
                print(mensaje_valueerror)
                time.sleep(1)
                
        if (control_venta==1):
            entrada="Galería"
            precio=20000
        elif (control_venta==2):
            entrada="Tribuna"
            precio=35000
        elif (control_venta==3):
            entrada="Cancha"
            precio=30000
        
        while True: # Validación cantidad de entradas
            os.system("cls")
            print(f"Ingresa la cantidad de las entradas de tipo {entrada}\n")
            
            try:
                cantidad = int(input("Ingresa tu opción:\n"))
                if (cantidad>0):
                    break
                else:
                    print(f"No puedes comprar {cantidad} entradas!")
                    time.sleep(1)
            except:
                print(mensaje_valueerror)
                time.sleep(1)
        
        while True: # Validación menú codigo de descuento
            os.system("cls")
            print(menu_codigo)
            
            try:
                control_codigo = int(input("Ingresa tu opción:\n"))
                if (1<=control_codigo<=2):
                    break
                else:
                    print(mensaje_outindex)
                    time.sleep(1)
            except:
                print(mensaje_valueerror)
                time.sleep(1)
        
        if (control_codigo==1):
            if (control_venta==1):
                descuento=0.9
                stringdescuento = f"Codido de descuento (10%) - Monto: ${round(precio*cantidad*(1-descuento), 0)}" # truncado a 0 decimales!
            elif (control_venta==2 or control_venta==3):
                descuento=0.95
                stringdescuento = f"Codigo de descuento (5%) - Monto: ${round(precio*cantidad*(1-descuento), 0)}" # truncado a 0 decimales!
        elif (control_codigo==2):
            stringdescuento=" "

        print(f"""--_ BOLETA _---
Tipo de entrada: {entrada} - Cantidad de entradas: {cantidad}
Subtotal: ${precio*cantidad}
{stringdescuento}
Total: ${precio*cantidad*descuento}
""")

        estadistica_ventas +=1
        if (control_venta==1):
            estadistica_galeria+=cantidad
            estadistica_vgaleria+=cantidad*precio
        elif (control_venta==2):
            estadistica_tribuna+=cantidad
            estadistica_vtribuna+=cantidad*precio
        elif (control_venta==3):
            estadistica_cancha+=cantidad
            estadistica_vcancha+=cantidad*precio
        
        if (control_codigo==1):
            estadistica_descuento+=1
        
        
        input(mensaje_enter)
    elif (control_principal==2):
        print("Menú de estadística")
        
        if (estadistica_ventas==0):
            print("No se han realizado transacciones!")
        else:
            print(f"""Cantidad de transacciones realizadas: {estadistica_ventas} - Total recaudado: ${estadistica_vgaleria+estadistica_vtribuna+estadistica_vcancha}
Cantidad de entradas de galería vendidas: {estadistica_galeria} - Recaudado: ${estadistica_vgaleria}
Cantidad de entradas de tribuna vendidas: {estadistica_tribuna} - Recaudado: ${estadistica_vtribuna}
Cantidad de entradas de cancha vendidas: {estadistica_cancha} - Recaudado: ${estadistica_vcancha}
Cantidad de ventas realizadas con descuento: {estadistica_descuento}
""")
        
        input(mensaje_enter)
    elif (control_principal==3):
        print("Saliendo...")
        time.sleep(1)
        break