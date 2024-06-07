import json
import os

archivo_path = "metro.json"

# Leemos un archivo
with open(archivo_path, "r", encoding='utf-8') as archivo:
    datos_json = json.load(archivo)

os.system("cls")
print("Ruta del archivo:", os.path.abspath(archivo_path), f"\n")

# que nos retorna esto?
#for caracteristica in datos_json:
#    print(caracteristica)

# Nos devuelve las llaves de los tres diccionarios.

#for caracteristica, elementos in datos_json.items(): # Iteramos en cada llave y valor
#    print (caracteristica) # Key del diccionario
#    print(elementos) # Value del diccionario (Retorna una lista)
#    print("---")

lista_lineas = []
lista_estaciones = []
lista_comunas = []
set_lineas = []
set_comunas = []

for llave, valor in datos_json.items():
    for i in range(len(valor)):
        if llave == "Nombre de la Línea":
            lista_lineas.append(valor[i])
        elif llave == "Nombre de la Estación":
            lista_estaciones.append(valor[i])
        elif llave == "Comuna":
            lista_comunas.append(valor[i])

set_comunas = list(set(lista_comunas))
set_lineas = list(set(lista_lineas))
set_comunas.sort() # comunas disponibles a mostrar (usos en selección)
set_lineas.sort() # lineas disponibles a mostrar (usos en selección)
cantidad = len(lista_lineas)
        
#print(lista_lineas)
#print(lista_estaciones)
#print(lista_comunas)
#print(set_lineas)
#print(set_comunas)

control = int(input(f"1. Mostrar todas las lineas\n2. Filtrar por Linea\n3. Filtrar por Comuna\n"))

if control==1:
    os.system("cls")
    for i in range(cantidad):
        print(lista_lineas[i], lista_estaciones[i], lista_comunas[i])
elif control==2:
    print(f"Selecciona la linea que deseas filtrar")
    for i in range(len(set_lineas)):
        print(f"{i+1}.- {set_lineas[i]}")
    
    linea = int(input(f""))

    os.system("cls")
    for i in range(cantidad):
        if lista_lineas[i] == set_lineas[linea-1]:
            print(lista_lineas[i], lista_estaciones[i], lista_comunas[i])
elif control==3:
    print(f"Selecciona la comuna que deseas filtrar")
    for i in range(len(set_comunas)):
        print(f"{i+1}.- {set_comunas[i]}")
    
    comuna = int(input(f""))

    os.system("cls")
    for i in range(cantidad):
        if lista_comunas[i] == set_comunas[comuna-1]:
            print(lista_lineas[i], lista_estaciones[i], lista_comunas[i])