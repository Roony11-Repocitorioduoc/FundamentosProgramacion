import os
import validar

def menu (lista_opciones, titulo):
    cant_elementos = len(lista_opciones)

    os.system("cls")
    print(titulo)
    for i in range(cant_elementos):
        print(f"{i+1}.- {lista_opciones[i]}")

def trabajadores(lista_trabajadores):
    cant_trabajadores = len(lista_trabajadores)
    os.system("cls")
    for i in range(cant_trabajadores):
        for k, v in lista_trabajadores[i].items():
            print(f"{k} - {v}")
        if (i<len(lista_trabajadores)-1):
            print("---")

def fichero(lista_trabajadores, lista_cargos): # Modo 0: Todos los registros - Modo 1: Por cargo
    nombre_archivo = "texto.txt"
    cant_trabajadores = len(lista_trabajadores)
    menu_impresion = ["Imprimir todos", "Impresión por cargo"]

    menu(menu_impresion, f"Menú Impresión")

    modo = validar.entero(f"\nIngrese la opción del menú\n")

    if modo==2:
        menu(lista_cargos, f"Selecciona el cargo a imprimir")

        control = validar.entero(f"\nIngrese la opción del menú\n")

    try:
        with open(nombre_archivo, 'w') as archivo:
            for i in range(cant_trabajadores):
                for k, v in lista_trabajadores[i].items():
                    if modo==1: # Todos los registros
                        archivo.write(f"{k} - {v}\n")
                    elif modo==2: # Por cargo
                        if ("Cargo" in lista_trabajadores[i] and lista_trabajadores[i]["Cargo"] == lista_cargos[control-1]):
                            archivo.write(f"{k} - {v}\n") 
                
                if (i<len(lista_trabajadores)-1):
                    archivo.write("---\n")

            print("Archivo creado exitosamente en:", os.path.abspath(nombre_archivo))
    except Exception as e:
        print(f"Error al crear el archivo: {e}")