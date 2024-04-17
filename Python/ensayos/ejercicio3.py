import os
import time

nombre_empresa = "PlasTic"

nombre_productos = {'Tazón':'500', 'Llavero':'200', 'Polera estampada':'3000'}
nombre_productos_mayorista = {'Tazón':'300', 'Llavero':'150', 'Polera estampada':'2000'}

cMayorista_1 = 100 # Cantidad mayorista del item 1
cMayorista_2 = 300 # Cantidad mayorista del item 2
cMayorista_3 = 50 # Cantidad mayorista del item 3

mayorista="" # Ingresar al modo mayorista
seleccion_principal="" # seleccion del articulo
producto="" # nombre del producto
precio=0 # precio del producto
cantidad=0 # cantidad del producto


mayorista=input(f"""Bienvenido a {nombre_empresa}
¿Quieres comprar como mayorista?
Tazón unidades > {cMayorista_1}
Llavero unidades > {cMayorista_2}
Polera unidades > {cMayorista_3}
    
(S/N)\n""").upper()

for item in range(len(nombre_productos)): # Print menu con valores del diccionario
    if (mayorista=="S"):
        print(f"{item+1}.-", [key for key in nombre_productos_mayorista.keys()][item], ": $", [value for value in nombre_productos_mayorista.values()][item])
    elif (mayorista=="N"):
        print(f"{item+1}.-", [key for key in nombre_productos.keys()][item], ": $", [value for value in nombre_productos.values()][item])
    


while True:
    seleccion_principal=input("¿Qué producto quieres?")

    # Ingresa los valores del producto seleccionado
    if (seleccion_principal.isdigit()):
        seleccion_principal=int(seleccion_principal)
        if (mayorista=="S" and (1 <= seleccion_principal <= len(nombre_productos_mayorista))):
            producto=[key for key in nombre_productos_mayorista.keys()][seleccion_principal-1]
            precio=[value for value in nombre_productos_mayorista.values()][seleccion_principal-1]
            break
        elif (mayorista=="N" and (1 <= seleccion_principal <= len(nombre_productos))):
            producto=[key for key in nombre_productos.keys()][seleccion_principal-1]
            precio=[value for value in nombre_productos.values()][seleccion_principal-1]
            break
        else:
            print("Ingresa un número valido!")
    else:
        print("Ingresa una cantidad valida (Número de opción valida)")
        
        
print(f"Seleccionaste: {producto} con un valor de ${precio}")

while True:
    while True:
        cantidad=input("Ingrese cantidad del producto")
        if (cantidad.isdigit()):
            cantidad=int(cantidad)
            break
        else:
            print("Ingresa un número entero!")
        
    
    if (mayorista=="S"):
        if ((seleccion_principal==1) and (cantidad<cMayorista_1)):
            print(f"La cantidad de {producto} debe ser mayor a {cMayorista_1}")
        else:
            break
        if ((seleccion_principal==2) and (cantidad<cMayorista_2)):
            print(f"La cantidad de {producto} debe ser mayor a {cMayorista_2}")
        else:
            break
        if ((seleccion_principal==3) and (cantidad<cMayorista_3)):
            print(f"La cantidad de {producto} debe ser mayor a {cMayorista_3}")
        else:
            break
    else:
        break
        

