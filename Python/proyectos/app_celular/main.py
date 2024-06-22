import os
import imprimir
import validar
import celular

# item menu
menu_principal = ["Agregar celular", "Listar celulares", "Buscar celulares", "Borrar celular", "Crear reporte", "Cargar datos generados"]

control = 0

# lista celulares
lista_celulares = []

while True:

    imprimir.menu(menu_principal, f"Opciones de menú", True)

    control = validar.entero(f"Ingresa la opción del menú\n")

    if control==len(menu_principal)+1:
        break
    elif control==1:
        print("a")
        lista_celulares.append(celular.agregar())
        os.system("pause")
    elif control==2:
        celular.listar(lista_celulares)
        os.system("pause")
    elif control==3:
        celular.busqueda(lista_celulares)
        os.system("pause")  
    elif control==4:
        celular.borrar(lista_celulares)
        os.system("pause")  
    elif control==5:
        celular.reporte(lista_celulares)
        os.system("pause")  
    elif control==6:
        celular.agregar_random(lista_celulares)
        os.system("pause")  