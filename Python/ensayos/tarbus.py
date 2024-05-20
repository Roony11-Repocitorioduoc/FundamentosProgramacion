import os
import time


# Variables
# - Main
opc_main="" # Manejo del menu principal
opc_venta="" # Manejo del menu venta
opc_pago="" # Manejo del metodo de pago
opc_ida="" # Manejo de ida y vuelta
valor_pasaje=0 # Valor inicial pasaje
destino_pasaje="" # Texto inicial pasaje
cantidad_pasaje="" # Cantidad pasaje
tipo_pasaje="" # Tipo pasaje

cantidad_abono="" # Control abono
subtotal=0 # Subtotal venta

# - Estadisticas
estadistica_recaudado=0 # total recaudado
estadistica_destino1=0 # ventas al destino 1
estadistica_destino2=0 # ventas al destino 2
estadistica_destin3=0 # ventas al destino 3

# - Textos
texto_empresa = "TarBas"
texto_main1 = "Vender pasaje"
texto_main2 = "Mostrar estadisticas"

texto_destino1 = "Curicó"
texto_destino2 = "Temuco"
texto_destino3 = "Puerto Montt"

texto_ventatitulo = "Menu Venta"
texto_estadisticatitulo = "Menu Estadistica"


texto_menusalir = "Salir"
texto_esperatecla = "Presiona ENTER para contunuar"
texto_errordigito = "Debes ingresar un digito!"
texto_erroroutindex = "Debes ingresar un digito dentro del rango del menú!"

while True:
    os.system("cls")
    print(f"""Menu aplicación {texto_empresa}.
1. {texto_main1}
2. {texto_main2}
3. {texto_menusalir}
Ingresa tu opción ahora: \n
""")
    
    while True:
        opc_main = input()
        
        if (opc_main.isdigit):
            opc_main = int(opc_main)
            if(1<=opc_main<=3):
                break    
            else:
                print(texto_erroroutindex)
        else:
            print(texto_errordigito)
    
    
    if (opc_main==1):
        os.system("cls")
        print(texto_ventatitulo)
        
        while True:
            os.system("cls")
            opc_venta = input(f"Ingresa cual es tu destino\n1. {texto_destino1} [$10000 | $18000]\n2. {texto_destino2} [$18000 | $30000]\n3. {texto_destino3} [$25000 | $40000]")
            
            if (opc_venta.isdigit):
                opc_venta = int(opc_venta)
                if(1<=opc_venta<=3):
                    break    
            else:
                print(texto_erroroutindex)
        else:
            print(texto_errordigito)
            
        while True:
            os.system("cls")
            opc_pago = input(f"¿Cuál es tu metodo de pago?\n1. Efectivo\n2. Débito\n(10% de desciento con efectivo en ida y vuelta)\nIngresa tu opción ahora: \n")
            
            if (opc_pago.isdigit):
                opc_pago = int(opc_pago)
                if(1<=opc_pago<=2):
                    break    
            else:
                print(texto_erroroutindex)
        else:
            print(texto_errordigito)
        
        while True:
            os.system("cls")
            opc_ida = input(f"¿Quieres tu pasaje de ida o ida y vuelta?\n1. Ida\n2. Ida y Vuelta\nIngresa tu opción ahora\n")
            
            if (opc_ida.isdigit):
                opc_ida = int(opc_ida)
                if(1<=opc_ida<=2):
                    break    
            else:
                print(texto_erroroutindex)
        else:
            print(texto_errordigito)
            
        if (opc_venta==1):
            destino_pasaje=texto_destino1
            estadistica_destino1+=1
            if (opc_ida):
                valor_pasaje=10000
                tipo_pasaje="Ida"
            else:
                valor_pasaje=18000
                tipo_pasaje="Ida y Vuelta"
        elif (opc_venta==2):
            destino_pasaje=texto_destino2
            estadistica_destino2+=1
            if (opc_ida):
                valor_pasaje=18000
                tipo_pasaje="Ida"
            else:
                valor_pasaje=30000
                tipo_pasaje="Ida y Vuelta"
        elif (opc_venta==3):
            destino_pasaje=texto_destino3
            estadistica_destin3+=1
            if (opc_ida):
                valor_pasaje=25000
                tipo_pasaje="Ida"
            else:
                valor_pasaje=40000
                tipo_pasaje="Ida y Vuelta"
            
        while True:
            cantidad_pasaje = input(f"Ingresa la cantidad de pasajes a comprar\n")
            
            if (cantidad_pasaje.isdigit):
                cantidad_pasaje = int(cantidad_pasaje)
                if(cantidad_pasaje>0):
                    break    
            else:
                print("Ingresa un número entero!")
        else:
            print(texto_errordigito)
         
        while True:
            os.system("cls")
            if (opc_pago==1):
                if (opc_pago==1 and opc_ida==2):
                    print(f"Total: {valor_pasaje*cantidad_pasaje}, Descuento: {valor_pasaje*cantidad_pasaje*0.1}, Total: {valor_pasaje*cantidad_pasaje*0.9}\n")
                    subtotal=valor_pasaje*cantidad_pasaje*0.9
                else:
                    print(f"Total: {valor_pasaje*cantidad_pasaje}\n")
                    subtotal=valor_pasaje*cantidad_pasaje
                cantidad_abono = input("Ingresa la cantidad con la que deseas pagar\n")
            
                if (cantidad_abono.isdigit):
                    cantidad_abono = int(cantidad_abono)
                    if(cantidad_abono>=subtotal):
                        break    
                    else:
                        print("Ingresa un valor mayor que el Subtotal")
                else:
                    print(texto_errordigito)
            else:
                break
            
        
        estadistica_recaudado += subtotal
            
        print(f""" Ticket de venta
Origen: Santiago, Destino: {destino_pasaje}, Valor Pasaje: {valor_pasaje}
Tipo de Boleto: {tipo_pasaje}, Cantidad: {cantidad_pasaje}
SubTotal: {valor_pasaje*cantidad_pasaje}
""")
        if (opc_pago==1 and opc_ida==2):
            if(cantidad_abono-subtotal)>0:
                print(f"Vuelto: {cantidad_abono-subtotal}")
            print(f"Descuento: {valor_pasaje*cantidad_pasaje*0.1}, Total: {valor_pasaje*cantidad_pasaje*0.9}")
        else:
            print(f"Total: {valor_pasaje*cantidad_pasaje}")
            
        
        input(texto_esperatecla)
    elif (opc_main==2):
        os.system("cls")
        print(texto_estadisticatitulo)
        
        if (estadistica_destino1+estadistica_destino2+estadistica_destin3>0):
            print(f"""
Cantidad recaudado: ${estadistica_recaudado}
Cantidad de pasajes vendidos: {estadistica_destino1+estadistica_destino2+estadistica_destin3}
Cantidad de pasajes a {texto_destino1}: {estadistica_destino1}
Cantidad de pasajes a {texto_destino2}: {estadistica_destino2}
Cantidad de pasajes a {texto_destino3}: {estadistica_destin3}
""")
        else:
            print("Realiza una venta primero!")
        
        input(texto_esperatecla)
    elif (opc_main==3):
        os.system("cls")
        print("Saliendo...")
        time.sleep("1")
        break


