import os
import time

## Datos de tabla
nombre_empresa = "Pizzota"
# Tamaños pizza
tipo_pizza1 = "Mediana"
tipo_pizza2 = "Familiar"
# Nombre de los tipos de pizza
pizza1 = "Napolitana"
pizza2 = "Vegetariana"
pizza3 = "Española"
# Nombre de los agregados
agregado1 = "Palos de ajo"
agregado2 = "Aros de cebolla"
# Valores de los agregados
vagregado1 = 3000
vagregado2 = 2200
# Valores pizzas medianas
valor_mpizza1 = 10000
valor_mpizza2 = 8000
valor_mpizza3 = 12000
# Valores pizzas grandes
valor_fpizza1 = 18000
valor_fpizza2 = 17000
valor_fpizza3 = 20000
# Controladores de menu
control_principal = 0
control_pizza = 0
control_tamaño = 0
control_agregado = 0
control_pago = 0
# Textos ticket
pizza = ""
valor = 0
valoragregado = 0
agregado = ""
pago = ""
# Estadísticas
totalrecaudado = 0
totalpizzas = 0


while True:
    # Reset de menús
    control_principal=0
    control_pizza=0
    control_agregado=0
    control_tamaño=0
    control_pago=0
    while True:
        os.system("cls")
        print(f"""---Menú Principal Pizzería {nombre_empresa}---
1. Vender Pizza
2. Ver Estadísticas
3. Salir
""")

        try:
            control_principal = int(input("Ingresa tu opción:\n"))
        
            if (1<=control_principal<=3):
                break
            else:
                print("ERROR! Ingresa un número dentro del rango del menú!")
                input("Presiona ENTER para continuar")
        except:
            print("ERROR! Ingresa un número entero")
            input("Presiona ENTER para continuar")
    
    
    if (control_principal==1):
        print("Menú Venta pizza")
        
        while True:
            os.system("cls")
            print(f"""Tipo Pizza\tValor pizza mediana\tValor pizza familiar
1. {pizza1}\t\t${valor_mpizza1}\t\t\t${valor_fpizza1}
2. {pizza2}\t\t${valor_mpizza2}\t\t\t${valor_fpizza2} 
3. {pizza3}\t\t${valor_mpizza3}\t\t\t${valor_fpizza3}              
""")
        
            try:
                control_pizza = int(input("Ingresa tu opción:\n"))
        
                if (1<=control_pizza<=3):
                    break
                else:
                    print("ERROR! Ingresa un número dentro del rango del menú!")
                    input("Presiona ENTER para continuar")
            except:
                print("ERROR! Ingresa un número entero")
                input("Presiona ENTER para continuar")
        while True:
            os.system("cls")
            print(f"""¿Quieres la pizza {tipo_pizza1} o {tipo_pizza2}?
1. Mediana
2. Familiar
""")
            try:
                control_tamaño = int(input("Ingresa tu opción:\n"))
        
                if (1<=control_tamaño<=2):
                    break
                else:
                    print("ERROR! Ingresa un número dentro del rango del menú!")
                    input("Presiona ENTER para continuar")
            except:
                print("ERROR! Ingresa un número entero")
                input("Presiona ENTER para continuar")
            
        if (control_pizza==1):
            pizza = pizza1
            valor = valor_mpizza1
            if (control_tamaño==2):
                valor = valor_fpizza1
        elif (control_pizza==2):
            pizza = pizza2
            valor = valor_mpizza2
            if (control_tamaño==2):
                valor = valor_fpizza2
        elif (control_pizza==3):
            pizza = pizza3
            valor = valor_mpizza3
            if (control_tamaño==2):
                valor = valor_fpizza3
        
        while True:
            os.system("cls")
            print(f"""¿Deseas agregar alguno de estos?
Agregado\t\tPrecio
1. {agregado1}\t\t$3000
2. {agregado2}\t$2200
3. Ambos\t\t$5200
4. Ninguno
""")
            try:
                control_agregado = int(input("Ingresa tu opción:\n"))
        
                if (1<=control_agregado<=4):
                    break
                else:
                    print("ERROR! Ingresa un número dentro del rango del menú!")
                    input("Presiona ENTER para continuar")
            except:
                print("ERROR! Ingresa un número entero")
                input("Presiona ENTER para continuar")
            
        if (control_agregado==1):
            valoragregado=3000
            agregado=agregado1
        elif (control_agregado==2):
            valoragregado=2200
            agregado=agregado1
        elif (control_agregado==3):
            valoragregado=5200
            agregado="Ambos"
        elif (control_agregado==4):
            valoragregado=0
            agregado="Ninguno"
        
        while True:
            os.system("cls")
            print(f"""¿Cual es tu medio de pago?
1. Efectivo (20% de descuento)
2. Débito
""")
            try:
                control_pago = int(input("Ingresa tu opción:\n"))
        
                if (1<=control_pago<=2):
                    break
                else:
                    print("ERROR! Ingresa un número dentro del rango del menú!")
                    input("Presiona ENTER para continuar")
            except:
                print("ERROR! Ingresa un número entero")
                input("Presiona ENTER para continuar")
        
        if (control_pago==1):
            pago="Efectivo"
        elif (control_pago==2):
            pago="Débito"
        
        print("--- Boleta ---")
        print(f"Tipo de pizza: {pizza}")
        if (control_tamaño==1):
            print("Tamaño: Mediana")
        else:
            print("Tamaño: Familiar")
        print(f"Valor pizza: ${valor}")
        if (1<=control_agregado<=3):
            print(f"Agregado: {agregado} | Valor: ${valoragregado}")
        print(f"Forma de pago: {pago}")
        if (control_pago==1):
            print(f"Total a pagar: ${valor+valoragregado*0.8}")
            print(f"Descuento: ${valor+valoragregado*0.2}")
        else:
            print(f"Total a pagar: ${valor+valoragregado}")
        
        if control_pago==1:
            totalrecaudado += valor+valoragregado*0.8
        else:
            totalrecaudado += valor+valoragregado
        totalpizzas += 1
        
        input("Presiona ENTER para continuar")
    elif (control_principal==2):
        os.system("cls")
        print("Menú Estadísticas")
        if (totalpizzas==0):
            print("No se han realizado ventas!")
        else:
            print(f"Total recaudado: ${totalrecaudado} | Pizzas vendidas: {totalpizzas}")
        
        input("Presiona ENTER para continuar")
    elif (control_principal==3):
        print("Saliendo...")
        time.sleep(1)
        break


        


