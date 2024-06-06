import imprimir
import validar

# Lista de strings
menu_principal = ["Registrar Trabajador", "Listar todos los trabajadores", "Imprimir planilla de sueldos", "Salir del programa"]
lista_cargos = ["Analista de Datos", "Desarrollador", "CEO"]

# Lista trabajadores
lista_trabajadores = []

# Variable de menú
control = 0

while True:
    imprimir.menu(menu_principal, f"Menú principal")

    control = validar.entero(f"\nIngrese la opción del menú\n")

    if control==1:
        lista_trabajadores.append(validar.ingreso_trabajador(lista_cargos))

        input(f"\nENTER\n")
    elif control==2:
        if (len(lista_trabajadores)>0):
            imprimir.trabajadores(lista_trabajadores)
        else:
            print(f"No hay trabajadores que mostrar!")

        input(f"\nENTER\n")
    elif control==3:

        if (len(lista_trabajadores)>0):
            imprimir.fichero(lista_trabajadores, lista_cargos)
        else:
            print(f"No hay trabajadores que mostrar!")



        input(f"\nENTER\n")
    elif control==4:
        break