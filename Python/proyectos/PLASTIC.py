import os
import time

# Vars
## Strings
nombre_empresa = "PlasTic"
nombre_producto1 = "Tazón"
nombre_producto2 = "Llavero"
nombre_producto3 = "Polera estampada"
## Precios
### General
valorG_producto1 = 800
valorG_producto2 = 500
valorG_producto3 = 5000
### Mayorista
valorM_producto1 = 500
valorM_producto2 = 300
valorM_producto3 = 3000

## Control de menús
control_principal = 0
control_venta = 0
control_socio = 0
control_pago = 0

## Strings mensaje usuario
mensaje_valueerror = "ERROR! Ingresa un número entero!"
mensaje_outindex = "ERROR! Ingresa un número que este en el menú!"
mensaje_tecla = "Presiona ENTER para continuar!"

## Variables venta
cantidad = 0
precio = 0
producto = ""
total = 0
pago = 0
descuento = 0
tipocliente = "GENERAL"
tipopago = ""

## Estadísticas
totalrecuadado = 0
totalvendido = 0

## Strings menús
menu_principal = f"""Aplicación de {nombre_empresa}
1. Venta de productos
2. Ver estadísticas
3. Salir
"""

menu_venta = f"""Producto\t\tValor General\tValor Socio
1. {nombre_producto1}\t\t${valorG_producto1}\t\t${valorM_producto1}
2. {nombre_producto2}\t\t${valorG_producto2}\t\t${valorM_producto2}
3. {nombre_producto3}\t${valorG_producto3}\t\t${valorM_producto3}
"""

menu_socio = f"""¿Es socio? (Precio especial)
1. Si
2. No
"""

menu_pago = f"""¿Cómo pagas? (Efectivo 20% de descuento)
1. Efectivo
2. Débito
"""


# Inicio loop
while True:
    # Reset vars menús
    control_principal=0
    control_venta = 0
    control_socio = 0
    tipocliente = "GENERAL"
    
    try: # principal
        os.system("cls")
        print(menu_principal)
        control_principal = int(input("Ingresa tu opción: \n"))
        if (not (1<=control_principal<=3)):
            print(mensaje_outindex)
            time.sleep(1)
    except:
        print(mensaje_valueerror)
        time.sleep(1)
        
    if (control_principal==1):

        while True: # venta
            try:
                os.system("cls")
                print("Menú venta")
                print(menu_venta)
                control_venta = int(input("Ingresa tu opción: \n"))
                if (not (1<=control_venta<=3)):
                    print(mensaje_outindex)
                    time.sleep(1)
                else:
                    break
            except:
                print(mensaje_valueerror)
                time.sleep(1)
        
        while True: # cantidad
            try:
                cantidad = int(input("Cuanto producto necesitas: \n"))
                if (cantidad<1):
                    print("No puedes llevar esa cantidad de producto!")
                else:
                    break
            except:
                print(mensaje_valueerror)
                
        while True: # socio
            try:
                os.system("cls")
                print("Menú venta")
                print(menu_socio)
                control_socio = int(input("Ingresa tu opción: \n"))
                if (not (1<=control_socio<=2)):
                    print(mensaje_outindex)
                    time.sleep(1)
                else:
                    break
            except:
                print(mensaje_valueerror)
                time.sleep(1)
        
        if (control_venta==1):
            producto=nombre_producto1
            precio=valorG_producto1
            if (control_socio==1):
                precio=valorM_producto1
                tipocliente="SOCIO"
        elif (control_venta==2):
            producto=nombre_producto2
            precio=valorG_producto2
            if (control_socio==1):
                precio=valorM_producto2
                tipocliente="SOCIO"
        elif (control_venta==3):
            producto=nombre_producto3
            precio=valorG_producto3
            if (control_socio==1):
                precio=valorM_producto3
                tipocliente="SOCIO"
        
        
        while True: # metodo de pago
            try:
                os.system("cls")
                print("Menú venta")
                print(menu_pago)
                control_pago = int(input("Ingresa tu opción: \n"))
                if (not (1<=control_pago<=2)):
                    print(mensaje_outindex)
                    time.sleep(1)
                else:
                    break
            except:
                print(mensaje_valueerror)
                time.sleep(1)
        
        if (control_pago==1):
            descuento=0.8
            tipopago=f"EFECTIVO descuento: ${cantidad*precio*(1-descuento)}"
        else:
            descuento=1
            tipopago="DÉBITO"
            
            
            
        ticket_compra = f"""--- TICKET DE COMPRA ---
Producto: {producto}
Cantidad de producto: {cantidad} - Tipo de cliente: {tipocliente}
Subtotal: ${cantidad*precio}
TIPO PAGO: {tipopago}
TOTAL: ${cantidad*precio*descuento}
"""

        print(ticket_compra)
        totalrecuadado+=(cantidad*precio*descuento)
        totalvendido+=cantidad
        
        time.sleep(1)
        input(mensaje_tecla)
    elif (control_principal==2):
        print("Menú Estadística")
        
        if (totalvendido==0):
            print("No se han realizado ventas!")
        else:
            print(f"Total recaudado: ${totalrecuadado} - Total de articulos vendidos: {totalvendido}")
        
        
        time.sleep(1)
        input(mensaje_tecla)
    elif (control_principal==3):
        print("Saliendo...")
        time.sleep(1)
        os.system("cls")
        break