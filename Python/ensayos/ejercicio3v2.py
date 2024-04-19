import os
import time

nombre_empresa = "PlasTic" # Nombre empresa de ventas
mensaje_numero = "Ingresa un número!\n" # mensaje de error no ingreso de numero
mensaje_outindex = "Ingresa una opción valida!\n" # mensaje error ingreso un número fuera de rango
nombre_productos = ["Tazón", "Llavero", "Polera estampada"] # nombre productos
medio_pago = ["Efectivo", "Débito"] # lista de nombre medios de pago
precio_detalle = [500, 200, 300] # precio detalle productos
precio_mayorista = [300, 150, 2000] # precio mayorista efectivo
unidades_mayorista = [100, 300, 50] # unidades para compra mayorista
seleccion_producto="" # seleccion de producto al principal
producto="" # producto seleccionado en la compra
precio="" # precio seleccionado en la compra
cantidad=0 # cantidad de producto en la compra
mpago="" # almacena el medio de pago
montoabonado=0 # solo si la compra es con efectivo se le dice al cliente con cuanto paga 
mayorista=False # define si es mayorista la compra
efectivo=False # define si es en efectivo el pago, caso contrario es débito


while True:
    time.sleep(1)
    os.system("cls")
    seleccion_producto = input(f"""Bienvenido a la tienda {nombre_empresa}\n
Selecciona uno de los siguientes productos: \n
1. {nombre_productos[0]} - ${precio_detalle[0]}
2. {nombre_productos[1]} - ${precio_detalle[1]}
3. {nombre_productos[2]} - ${precio_detalle[2]}
\n""")
    
    if (seleccion_producto.isdigit()):
        seleccion_producto=int(seleccion_producto)
        if (1<= seleccion_producto<= len(nombre_productos)):
            producto=nombre_productos[seleccion_producto-1]
            break
        else:
            print(mensaje_outindex)
            input("\n Presiona ENTER para continuar")
    else:
        print(mensaje_numero)
        input("\n Presiona ENTER para continuar")

while True:
    os.system("cls")
    cantidad = input(f"Ingresa la cantidad de: {nombre_productos[seleccion_producto-1]}\n")

    if (cantidad.isdigit()):
        cantidad=int(cantidad)
        if (cantidad>= unidades_mayorista[seleccion_producto-1]):
            precio=precio_mayorista[seleccion_producto-1]
            mayorista=True
            break
        else:
            precio=precio_detalle[seleccion_producto-1]
            mayorista=False
            break
    else:
        print(mensaje_numero)
        input("\n Presiona ENTER para continuar")

os.system("cls")

print(f"""Articulo: {producto}, precio: ${precio}, Cantidad: {cantidad}
      Subtotal: ${precio*cantidad}
      \n""")
if (mayorista):
    print("Compra mayorista!\n")
else:
    print("Compra al detalle!\n")

input("\n Presiona ENTER para continuar")


while True:
    os.system("cls")

    mpago = input(f"""Ingresa el medio de pago:
1. {medio_pago[0]}
2. {medio_pago[1]}
""")
    if (mayorista):
        print(f"Si pagas con {medio_pago[0]}, obtendras un 10$ de descuento al final de tu boleta\n")
    
    if(mpago.isdigit()):
        mpago=int(mpago)
        if (1<= mpago<= len(medio_pago)):
            print(f"Medio de pago seleccionado: {medio_pago[mpago-1]}\n")
            if (mpago==1):
                efectivo=True
                break
            else:
                efectivo=False
                break
        else:
            print(mensaje_outindex)
            input("\n Presiona ENTER para continuar")
    else:
        print(mensaje_numero)
        input("\n Presiona ENTER para continuar")
        
if (efectivo):
    while True:
        os.system("cls")
        montoabonado = input(f"Ingrese la cantidad que desea abonar\n Subtotal: ${cantidad*precio}\n")
        
        if (montoabonado.isdigit):
            montoabonado=int(montoabonado)
            if (montoabonado<(precio*cantidad)):
                print("No es suficiente dinero!\n")
                input("\n Presiona ENTER para continuar")
            else:
                break
        else:
            print(mensaje_numero)
            input("\n Presiona ENTER para continuar")

os.system("cls")
print(f"""*** Boleta ***
Producto: {producto}, Cantidad: {cantidad}, Valor: {precio}
Subtotal: {cantidad*precio}, , Medio de pago: {medio_pago[mpago-1]}
""")
if (efectivo):
    if(montoabonado!=(cantidad*precio)):
        print(f"Monto abonado: ${montoabonado}")
        if (mayorista):
            print(f"Vuelto: ${montoabonado-(cantidad*precio*0.9)}")
        else:
            print(f"Vuelto: ${montoabonado-(cantidad*precio)}")
    if (mayorista):
        print(f"Descuento: ${cantidad*precio*0.1}\nTotal: ${cantidad*precio*0.9}")
else:
    print(f"Total: ${cantidad*precio}")


        

        


