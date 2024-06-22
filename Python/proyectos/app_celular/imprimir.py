import os
import json
import csv

def menu(menu_items, title, exit):
    os.system("cls")
    print(title)
    for k in range(len(menu_items)):
        print(f"{k+1}.- {menu_items[k]}")
    if exit:
        print(f"{len(menu_items)+1}.- Salir")

def reporte_json(nombre, lista_datos):
    with open(nombre, "w", encoding="utf-8") as archivo:
        try:
            json.dump(lista_datos, archivo, indent=4, ensure_ascii=False)
            print(f"Archivo creado correctamente en: {os.path.abspath(nombre)}")
        except Exception as e:
            print(f"No se ha creado el archivo: {e}")

def reporte_csv(nombre, lista_datos):
    lista_keys = []
    # Lista Keys
    for k in lista_datos[0].keys():
        lista_keys.append(k)

    with open(nombre, "w", encoding="utf-8") as archivo:
        try:
            writer = csv.writer(archivo)

            writer.writerow(lista_keys)

            for k in range(len(lista_datos)):
                fila = []
                for i in range(len(lista_keys)):
                    fila.append(lista_datos[k][lista_keys[i]])
                writer.writerow(fila)
            print(f"Archivo creado correctamente en: {os.path.abspath(nombre)}")
        except Exception as e:
            print(f"No se ha creado el archivo: {e}")

        
