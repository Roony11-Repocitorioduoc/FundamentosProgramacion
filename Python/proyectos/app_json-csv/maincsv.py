import csv
import json
import os

lista_imc = []
lista_carac = []
lista_dict = []

def imc(peso, estatura, lista_imc):
    lista_imc.append(round(peso/estatura**2, 1))
    
def caracterizacion(imc):
    categorizacion = ""
    
    if imc<16:
        categorizacion="Infrapeso: Delgadez severa"
    elif 16<=imc<17:
        categorizacion="Infrapeso: Delgadez moderada"
    elif 17<=imc<18.5:
        categorizacion="Infrapeso: Delgadez aceptable"
    elif 18.5<=imc<25:
        categorizacion="Peso nomral"
    elif 25<=imc<30:
        categorizacion="Sobrepeso"
    elif 30<=imc<35:
        categorizacion="Obeso: Tipo I"
    elif 35<=imc<40:
        categorizacion="Obeso: Tipo II"
    elif 40<=imc:
        categorizacion="Obeso: Tipo III"
        
    return categorizacion


# Abrimos el archivo csv
with open("usuarios_ficticios.csv", "r", encoding="utf-8") as archivo:
    # Los cargamos en datos_csv, DictReader devuelve un diccionario al leer el archivo
    datos_csv = csv.DictReader(archivo)
    
    i = 0
    os.system("cls")
    
    for fila in datos_csv:
        nombre = fila["nombre"]
        peso = int(fila["peso"])
        estatura = float(fila["estatura"])
        
        imc(peso, estatura, lista_imc)
        
        lista_carac.append(caracterizacion(lista_imc[i]))
        
        print(f"{nombre} - {peso} - {estatura} - {round(lista_imc[i])} - {lista_carac[i]}")
        
        dict = {
            "nombre" : nombre,
            "peso" : peso,
            "estatura" : estatura,
            "imc" : round(lista_imc[i]),
            "categorizacion" : lista_carac[i]
        }
        
        lista_dict.append(dict)
        
        i+=1
    
    # Limpiamos listas temporales de datos
    lista_carac.clear()
    lista_imc.clear()

with open("usuarios_ficticios.json", "w", encoding="utf-8") as archivo:
    # Escribimos los diccionarios en un json
    json.dump(lista_dict, archivo, indent=4)