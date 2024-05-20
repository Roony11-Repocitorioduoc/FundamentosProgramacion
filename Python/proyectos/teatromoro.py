import os
import time


# Variables
## Main
funcion1_valorG = 15000
funcion1_valorE = 10000
funcion2_valorG = 18000
funcion2_valorE = 12000
funcion3_valorG = 20000
funcion3_valorE = 15000

control_principal = 0
control_funcion = 0
control_estudiante = 0
control_descuento = 0

funcion = ""
entrada = ""
descuentoN = ""
descuento = 0.0
cantidad = 0
valor = 0

## Estadisticas

cantidad_entradas = 0
cantidad_recaudado = 0

## Textos
funcion_dia1 = "Viernes"
funcion_dia2 = "Sabado"
funcion_dia3 = "Domingo"

funcion_entrada1 = "Gerenal"
funcion_entrada2 = "Estudiante"

descuento_entel = "Zona Entel"
descuento_gas = "Club Metrogas"

while True:
    os.system("cls")
    print(f"""---- MENÚ ----
1. Compra de entradas
2. Ver estadisticas
3. Salir\n
""")
    try:
       while True:
           control_principal = int(input("Ingresa la opción\n"))
           if (control_principal>3 or control_principal<1):
               print("Error, Ingresa los digitos presentados en el menú!")
               time.sleep(1)
           else:
               break
    except:
        print("Error, Ingresa solo números!")
        time.sleep(1)
    
    if (control_principal==1):
        os.system("cls")
        print("Menu Venta\n")
        
        print(f"""Selecciona la función que deseas asistir
1. {funcion_dia1}
2. {funcion_dia2}
3. {funcion_dia3}
""")
    
        try:
            while True:
                control_funcion = int(input("Ingresa la opción\n"))
                if (control_funcion>3 or control_funcion<1):
                    print("Error, Ingresa los digitos presentados en el menú!")
                    time.sleep(1)
                else:
                    break
        except:
            print("Error, Ingresa solo números!")
            time.sleep(1)
        
        os.system("cls")
        print(f""" ¿Eres estudiante?
1. Si
2. No
""")
        try:
            while True:
                control_estudiante = int(input("Ingresa la opción\n"))
                if (control_estudiante>2 or control_estudiante<1):
                    print("Error, Ingresa los digitos presentados en el menú!")
                    time.sleep(1)
                else:
                    break
        except:
            print("Error, Ingresa solo números!")
            time.sleep(1)
            
        os.system("cls")
        try:
            while True:
                cantidad = int(input("Ingresa la cantidad\n"))
                if (cantidad<1):
                    print("Error, Ingresa una cantidad mayor a 0!")
                    time.sleep(1)
                else:
                    break
        except:
            print("Error, Ingresa solo números!")
            time.sleep(1)
        
        cantidad_entradas+=cantidad
        
        if control_funcion==1:
            funcion=funcion_dia1
            valor=funcion1_valorG
            entrada=funcion_entrada1
            if control_estudiante == 1:
                valor=funcion1_valorE
                entrada=funcion_entrada2
        elif control_funcion==2:
            funcion=funcion_dia2
            valor=funcion2_valorG
            entrada=funcion_entrada1
            if control_estudiante == 1:
                valor=funcion2_valorE
                entrada=funcion_entrada2
        elif control_funcion==3:
            funcion=funcion_dia3
            valor=funcion3_valorG
            entrada=funcion_entrada1
            if control_estudiante == 1:
                valor=funcion3_valorE
                entrada=funcion_entrada2
               
        os.system("cls")
        print(f"""Subtotal: {valor*cantidad}
Cantidad de entradas: {cantidad}, Día función: {funcion}, Tipo de entrada: {entrada}
¿Cuentas con alguno de los siguientes descuentos?
1. {descuento_entel} (30%)
2. {descuento_gas} (10%)
3. Ningun descuento
""")
        
        try:
            while True:
                control_descuento = int(input("Ingresa la opción\n"))
                if (control_descuento<1 or control_descuento>3):
                    print("Error, Ingresa los digitos presentados en el menú!")
                    time.sleep(1)
                else:
                    break
        except:
            print("Error, Ingresa solo números!")
            time.sleep(1)
        
        if (control_descuento==1):
            descuentoN=descuento_entel
            descuento=0.7
        elif (control_descuento==2):
            descuentoN=descuento_gas
            descuento=0.9
        elif (control_descuento==3):
            descuentoN="Ninguno"
            descuento=1
            
        os.system("cls")
        print(f"""Subtotal: {valor*cantidad}
Cantidad de entradas: {cantidad}, Día función: {funcion}, Tipo de entrada: {entrada}
Tipo de descuento: {descuentoN}, Cantidad de descuento: {valor*cantidad*(1-descuento)}
Total: {valor*cantidad*descuento}
""")
        cantidad_recaudado+=valor*cantidad*descuento
        
        input("Preciona ENTER para continuar")
    elif (control_principal==2):
        print("Menu Estadistica\n")
        
        if (cantidad_entradas==0):
            print("Primero realiza alguna transacción!")
        else:
            print(f"Cantidad de entradas vendidas: {cantidad_entradas}, Total recaudado: ${cantidad_recaudado}")
        
        input("Preciona ENTER para continuar")
    elif (control_principal==3):
        os.system("cls")
        print("Saliendo.")
        time.sleep(0.7)
        os.system("cls")
        print("Saliendo..")
        time.sleep(0.7)
        os.system("cls")
        print("Saliendo...")
        time.sleep(0.7)
        break