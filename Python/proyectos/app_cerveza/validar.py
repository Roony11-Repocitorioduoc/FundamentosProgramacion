import datetime
import imprimir
import os

def decimal(titulo):
    while True:
        try:
            variabledecimal = float(input(titulo))
            return variabledecimal
        except:
            continue

def entero(titulo):
    while True:
        try:
            variableentera = int(input(titulo))
            return variableentera
        except:
            continue

def cerveza(lista_estilo):
    fecha_actual = f"{datetime.datetime.now()}" # Fecha actual de la maquina para el registro.

    codigo = "" # Codigo de la cerveza.

    while len(codigo)!=3:
        os.system("cls")
        codigo = input(f"Ingresa el codigo de la cerveza (3 digitos)\n").strip().upper()

    nombre = "" # Nombre de la cerveza.

    while len(nombre)<=0:
        os.system("cls")
        nombre = input(f"Ingresa el nombre de la cerveza\n")
    
    precio = 0.0 # Precio de la cerveza

    while precio<=0:
        os.system("cls")
        precio = decimal(f"Ingresa el precio de la cerveza\n")
    
    pais_origen = "" # País de origen de la cerveza

    while len(pais_origen)<=0:
        os.system("cls")
        pais_origen = input(f"Ingresa el país de origen\n")
    
    estilo = "" # Estilo de la cerveza
    control = 0 # Control del menú

    while not 1<=control<=len(lista_estilo):
        imprimir.menu(lista_estilo)

        control = entero(f"Ingresa tu opción\n")

    estilo = lista_estilo[control-1]

    os.system("cls")
    grado = decimal(f"Ingresa la graduación de tu bebida\n")

    comentario_añadir = ""

    while len(comentario_añadir)<=0:
        os.system("cls")
        comentario_añadir = fecha_actual + f" -> añadida ; Cerveza: {nombre} " + input(f"Agrega comentarios\n")
    
    cerveza = {
        "Codigo" : codigo,
        "Nombre" : nombre,
        "Precio" : precio,
        "Pais Origen" : pais_origen,
        "Estilo" : estilo,
        "AVB" : grado,
        "Comentario" : comentario_añadir
    }

    return cerveza
    




    



    


    