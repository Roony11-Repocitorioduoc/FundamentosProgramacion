import validar
import imprimir
import os
import modulo_venta_gas

menu_principal = ["Crear BD de Ventas", "Lista Ventas", "Crear Reporte", "Estadisticas", "(En Contruccion)"]

lista_gas = [] # Guarda dict de los gases generados

# Menu principal
control = 0

# Strings
ingreso_opc = f"Ingresa la opción del menú\n"

while True:
    imprimir.menu(menu_principal, f"Menu principal", True)
    
    control = validar.entero(ingreso_opc)
    
    if control == 1:
        print(menu_principal[0])
        lista_gas = modulo_venta_gas.cargar_data_test()
        os.system("pause")
    elif control == 2:
        print(menu_principal[1])
        modulo_venta_gas.listar_ventas_list(lista_gas)
        os.system("pause")
    elif control == 3:
        print(menu_principal[2])
        modulo_venta_gas.imprimir_csv(lista_gas)
        os.system("pause")
    elif control == 4:
        print(menu_principal[3])
        
        os.system("pause")
    elif control == 5:
        print(menu_principal[4])
        
        os.system("pause")
    elif control == 6:
        break
    else:
        print(f"Ingresa una opción valída!")
        
        os.system("pause")