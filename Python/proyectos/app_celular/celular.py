import os
import validar
import random
import imprimir

def agregar():
    numero = ""
    marca = ""
    modelo = ""
    compañia = ""

    while not 1<=len(numero)<=9:
        os.system("cls")
        numero = input(f"Ingresa el número del celular\nMáximo 9 digitos\n").strip().lower()

    while not 1<=len(marca):
        os.system("cls")
        marca = input(f"Ingresa la marca del celular\n").strip().lower()

    while not 1<=len(modelo):
        os.system("cls")
        modelo = input(f"Ingresa el modelo del celular\n").strip().lower()

    while not 1<=len(compañia):
        os.system("cls")
        compañia = input(f"Ingresa ingresa la compañia del celular\n").strip().lower()

    celular = {
        "numero": numero,
        "marca": marca,
        "modelo": modelo,
        "compañia": compañia
    }

    return celular

def agregar_random(lista_celulares):
    lista_numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lista_marca = ["supercelular", "optimus", "atron"]
    lista_modelo = ["aa1", "aa2", "xm23", "145a"]
    lista_compañia = ["wom", "entel", "claro", "movistar"]

    cant_agregar = random.randrange(1, random.randrange(2, 14))

    # Creamos el celular
    os.system("cls")
    for c in range(cant_agregar):
        numero = ""
        marca = ""
        modelo = ""
        compañia = ""

        for n in range(random.randrange(1, 9)):
            numero = numero+lista_numeros[random.randrange(0, 9)]
        
        marca = lista_marca[random.randrange(0, len(lista_marca)-1)]

        modelo = lista_modelo[random.randrange(0, len(lista_modelo)-1)]

        compañia = lista_compañia[random.randrange(0, len(lista_compañia)-1)]

        celular = {
            "numero": numero,
            "marca": marca,
            "modelo": modelo,
            "compañia": compañia
        }

        lista_celulares.append(celular)

    print(f"Se han agregado {cant_agregar} celulares!")




def listar(lista_celulares):
    if len(lista_celulares)==0:
        print(f"No hay celulares que mostrar")
        return
    
    for k in range(len(lista_celulares)):
        print(f"""{k+1}.- Marca: {lista_celulares[k]["marca"]} - Modelo: {lista_celulares[k]["modelo"]}
Compañia: {lista_celulares[k]["compañia"]} - Número: +56{lista_celulares[k]["numero"]}
""")
        
def filtrar(lista_celulares):
    if len(lista_celulares)==0:
        print(f"No hay celulares que mostrar")
        return

    lista_keys = []
    lista_atributos = []

    lista_id = []

    # Rellena la lista con todas las keys
    for k in lista_celulares[0].keys():
        lista_keys.append(k)

    imprimir.menu(lista_keys, f"Por que elemento deseas filtrar", False)

    llave = 0

    while not 1<=llave<=len(lista_keys):
        llave = validar.entero(f"Ingresa la opción del menú\n")
    
    for k in range(len(lista_celulares)):
        lista_atributos.append(lista_celulares[k][lista_keys[llave-1]])

    # normalizamos la lista
    lista_atributos = list(set(lista_atributos))
    lista_atributos.sort()

    imprimir.menu(lista_atributos, f"Selecciona {lista_keys[llave-1]} a filtrar", False)

    atributo = 0

    while not 1<=atributo<=len(lista_atributos):
        atributo = validar.entero(f"Ingresa la opción del menú\n")

    # Encontremos y filtremos el celular

    for k in range(len(lista_celulares)):
        if lista_celulares[k][lista_keys[llave-1]]==lista_atributos[atributo-1]:
            lista_id.append(k) # lista que guarda los id de la lista grande
    
    # limpieza de listas
    lista_keys  = []
    lista_atributos = []

    return lista_id

def busqueda(lista_celulares):
    if len(lista_celulares)==0:
        print(f"No hay celulares que mostrar")
        return

    lista_id = filtrar(lista_celulares) # cargamos lo que necesitamos

    print(f"Hay {len(lista_id)} celulares que corresponden al filtro seleccionado")
    os.system("pause")

    os.system("cls")
    for k in range(len(lista_id)):
        print(f"""{k+1}.- Marca: {lista_celulares[lista_id[k]]["marca"]} - Modelo: {lista_celulares[lista_id[k]]["modelo"]}
Compañia: {lista_celulares[lista_id[k]]["compañia"]} - Número: +56{lista_celulares[lista_id[k]]["numero"]}
""")

def borrar(lista_celulares):
    if len(lista_celulares)==0:
        print(f"No hay celulares que mostrar")
        return
    
    lista_id = filtrar(lista_celulares)
    print(f"Hay {len(lista_id)} celulares que corresponden al filtro seleccionado")
    os.system("pause")

    os.system("cls")
    print(f"Selecciona el celular a borrar")
    for k in range(len(lista_id)):
        print(f"""{k+1}.- Marca: {lista_celulares[lista_id[k]]["marca"]} - Modelo: {lista_celulares[lista_id[k]]["modelo"]}
Compañia: {lista_celulares[lista_id[k]]["compañia"]} - Número: +56{lista_celulares[lista_id[k]]["numero"]}
""")
    borrador = 0

    while not 1<=borrador<=len(lista_id):
        borrador = validar.entero(f"Selecciona el celular\n")
    
    os.system("cls")
    print(f"""Seguro que quieres borrar a:
Marca: {lista_celulares[lista_id[borrador-1]]["marca"]} - Modelo: {lista_celulares[lista_id[borrador-1]]["modelo"]}
Compañia: {lista_celulares[lista_id[borrador-1]]["compañia"]} - Número: +56{lista_celulares[lista_id[borrador-1]]["numero"]}
1. Si
2. No
""")
    
    borrar = 0

    while not 1<=borrar<=2:
        borrar = validar.entero(f"Ingresa la opción del menú\n")

    if borrar==1:
        lista_celulares.pop(lista_id[borrador-1])
    else:
        return

def reporte(lista_celulares):
    if len(lista_celulares)==0:
        print(f"No hay celulares que mostrar")
        return
    
    nombre = ""
    while not 1<=len(nombre):
        nombre = input(f"Ingresa el nombre del archivo\n").lower().strip()
    
    os.system("cls")
    print(f"Que tipo de archivo deseas generar\n1. JSON\n2. CSV\n")

    eleccion = 0

    while not 1<=eleccion<=2:
        eleccion = validar.entero(f"Ingresa la opción del menú\n")

    if eleccion==1:
        nombre = nombre+".json"
        imprimir.reporte_json(nombre, lista_celulares)
    elif eleccion==2:
        nombre = nombre+".csv"
        imprimir.reporte_csv(nombre, lista_celulares)





    