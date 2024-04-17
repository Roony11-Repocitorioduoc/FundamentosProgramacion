import os
import time

nombre_empresa = "PlasTic"

nombre_productos = {'Tazón':500, 'Llavero':200, 'Polera estampada':3000}
nombre_productos_mayorista = {'a':300, 'b':150, 'c':2000}

cMayorista_1 = 100 # Cantidad mayorista del item 1
cMayorista_2 = 300 # Cantidad mayorista del item 2
cMayorista_3 = 50 # Cantidad mayorista del item 3

cProducto = [cMayorista_1, cMayorista_2, cMayorista_3]

tPago = ["Efectivo", "Débito"]

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
Descuento 10% al pagar con efectivo
(S/N)\n""").upper()

for item in range(len(nombre_productos)): # Print menu con valores del diccionario
    if (mayorista=="S"):
        print(f"{item+1}.-", [key for key in nombre_productos.keys()][item], ": $", [value for value in nombre_productos_mayorista.values()][item])
        tipo_compra="Mayorista"
    elif (mayorista=="N"):
        print(f"{item+1}.-", [key for key in nombre_productos.keys()][item], ": $", [value for value in nombre_productos.values()][item])
        tipo_compra="Detalle"
    


while True:
    seleccion_principal=input("¿Qué producto quieres?\n")

    # Ingresa los valores del producto seleccionado
    if (seleccion_principal.isdigit()):
        seleccion_principal=int(seleccion_principal)
        producto=[key for key in nombre_productos.keys()][seleccion_principal-1]
        if (mayorista=="S" and (1 <= seleccion_principal <= len(nombre_productos_mayorista))):
            precio=[value for value in nombre_productos_mayorista.values()][seleccion_principal-1]
            break
        elif (mayorista=="N" and (1 <= seleccion_principal <= len(nombre_productos))):
            precio=[value for value in nombre_productos.values()][seleccion_principal-1]
            break
        else:
            print("Ingresa un número valido\n")
    else:
        print("Ingresa una cantidad valida (Número de opción valida)\n")
        
        
print(f"Seleccionaste: {producto} con un valor de ${precio}\n")

while True:
        
    cantidad=input("Ingrese cantidad del producto:\n")

    if (cantidad.isdigit()):
        cantidad=int(cantidad)
        if (mayorista=="S"):
            if (cProducto[seleccion_principal-1]>cantidad):
                print(f"La cantidad de {producto} debe ser mayor o igual a {cProducto[seleccion_principal-1]}\n")
            else:
                break
        else:
            break
    else:
        print("Ingresa un número entero!\n")

while True:
    print("Ingresa el medio de pago")
    for menu in range(len(tPago)):
        print(f"{menu+1}.- {tPago[menu]}")
    
    tipo_pago = input()

    if (tipo_pago.isdigit()):
        tipo_pago=int(tipo_pago)
        if (1<= tipo_pago<= len(tPago)):
            break
        else:
            print("Ingresa una opción valida!")
    else:
        print("Ingresa una cantidad valida (Número de opción valida)\n")

if (tipo_pago==1 and mayorista=="S"):
    print (f"Subtotal: {precio*cantidad*0.9}\n")
else:
    print(f"Subtotal: {precio*cantidad}\n")

while True:
    if (tipo_pago==1):
        abono_compra=str(input("¡Con cuanto dinero pagas?\n"))
        if (abono_compra.isdecimal()):
            abono_compra=float(abono_compra)
            if (abono_compra<precio*cantidad):
                print("Ingresa una cantidad igual o mayor al total")
            else:
                break
        else:
            print("Ingresa un valor valido!")


print(f"""*** Ticket de Boleta ***
Producto: {producto}, Valor: {precio}, Cantidad: {cantidad}
Subtotal: {precio*cantidad}
"Tipo de compra: {tipo_compra}, Tipo de pago: {tPago[tipo_pago-1]}""")
if (tipo_pago==1):
    print(f"Vuelto: {abono_compra-(precio*cantidad)}")
    if (mayorista=="S"):
        print(f"Descuento 10%, Total: {precio*cantidad*0.9}")
    else:
        print(f"Total: {precio*cantidad}")
elif (tipo_pago==2):
    print(f"Total: {precio*cantidad}")
        

