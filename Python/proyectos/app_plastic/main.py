import validacion
import menu
import os

# Listas
menu_bool = ["Si", "No"]
menu_principal = ["Vender productos", "Agregar productos", "Eliminar productos"]
nombre_productos = ["Tazón", "Llavero", "Polera estampada"]
precio_productos = [800, 500, 500, 300, 5000, 3000] # duos de valores EJEMPLO (0 - 1) Valores general y especial de tazón


# Control de menu
control = 0
control_menu = 0

# Flags
socio = False

# Venta
cantidades = []
subtotales = []
cantidad = 0
subtotal = 0

while True:
    # Reset
    socio = False
    subtotal = 0

    menu.mostrar(menu_principal, f"Ingresa tu opción 0 - {len(menu_principal)}", "SI")

    control_menu = validacion.entero(control, f"Ingresa tu opción\n")

    # Menu Principal
    if (control_menu==0):
        break
    elif (control_menu==1):
        if (len(nombre_productos)<=0):
            print("No hay elementos que vender!")
            input("ENTER")
            continue

        menu.mostrar(menu_bool, f"Eres Socio de la tienda?", "NO")

        control_menu = validacion.entero(control, f"Ingresa tu opción\n")
        # Menu Socio
        if (control_menu==1):
            socio = True

        elif (control_menu==2):
            socio = False
        else:
            print("Ingresa una opción valida!")
            input("ENTER")

        # Creacion lista de cantidades y subtotales para cada elemento
        for i in range(len(nombre_productos)):
            cantidades.append(0)
            subtotales.append(0)

        while True:
            os.system("cls")
            # Listado de los productos para comprarlos junto a su cantidad
            k=0
            for i in range(0, len(precio_productos), 2):
                if socio:
                    subtotales[k] = cantidades[k]*precio_productos[i+1]
                    print(f"{k+1}.- Producto: {nombre_productos[k]} - Valor socio: ${precio_productos[i+1]} - total: ${subtotales[k]}", end=" - ")
                else:
                    subtotales[k] = cantidades[k]*precio_productos[i]
                    print(f"{k+1}.- Producto: {nombre_productos[k]} - Valor: ${precio_productos[i]} - total: ${subtotales[k]}", end=" - ")
                
                print(f"Cantidad: {cantidades[k]}")
                k+=1
            
            subtotal = sum(subtotales)
            print(f"\nSubtotal: ${subtotal}\n")
            print(f"0.- Continuar\n")
        
            control_menu = validacion.entero(control, f"Ingresa tu opción\n")
            # Menu Productos
            if (control_menu==0):
                break
            elif (control_menu>len(nombre_productos) or control_menu<0):
                print("Ingresa una opción valida!")
            else:
                validacion.cantidad(cantidad, control_menu, nombre_productos, cantidades)
            




        input("ENTER")
    
    else:
        print("Ingresa una opción valida!")
        input("ENTER")
            






