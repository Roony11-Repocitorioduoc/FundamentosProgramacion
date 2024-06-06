import os
import time
import imprimir

def entero(titulo):
    while True:
        try:
            variableentera = int(input(titulo))
            return variableentera
        except ValueError:
            print(f"Error, debes ingresar un número entero!")
            time.sleep(1)

def decimal(titulo):
    while True:
        try:
            variabledecimal = float(input(titulo))
            return variabledecimal
        except ValueError:
            print(f"Error, debes ingresar un número decimal!")
            time.sleep(1)

def ingreso_trabajador(lista_cargos):
    cant_cargos = len(lista_cargos)
    trabajador = {} # Dict vacio para datos del trabajador

    # Ingreso del nombre del trabajador
    nombre = str(input(f"Ingresa el nombre del trabajador\n")).lower().strip()

    # Ingreso cargo - Ingreso de menú de solo las opciones disponibles
    while True:
        imprimir.menu(lista_cargos, f"Seleccione el cargo del trabajador\n")

        j = entero(f"\nIngrese la opción del menú\n")

        if (1<=j<=cant_cargos):
            cargo = lista_cargos[j-1]
            break
        else:
            print(f"Error, esa opción no esta en el menú!")
            time.sleep(1)
    
    # Ingreso del sueldo bruto
    minimo = 1

    while True:
        sueldo = decimal(f"Ingresa el sueldo del trabajador\n")

        if (sueldo>=minimo):
            break
        else:
            print(f"Error, ingresa un sueldo valido!")
    
    # Descuentos legales (Descuento Salud = 7%, Descuento AFP = 12%)
    desc_salud = 0.07
    desc_afp = 0.12

    salud = sueldo*desc_salud
    afp = sueldo*desc_afp

    sueldo_liquido = sueldo-(salud+afp)

    # Ingreso de los usuarios al diccionario
    dict = {
        "Trabajador" : nombre,
        "Cargo" : cargo,
        "Sueldo Bruto" : round(sueldo),
        "Descuento Salud" : round(salud),
        "Descuento AFP" : round(afp),
        "Sueldo liquido" : round(sueldo_liquido)
    }

    return dict


