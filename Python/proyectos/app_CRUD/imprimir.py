import os
import time
import validar
import json

def menu(lista_menu, salir):
    os.system("cls")
    for i in range(len(lista_menu)):
        print(f"{i+1}.- {lista_menu[i]}")
        
        # Añade X.- Salir al final del menú segun requerimiento, salir = True (Aparece)
    if salir:
        print(f"{len(lista_menu)+1}.- Salir")
            
    return validar.entero(f"Ingresa la opción del menú\n")

def lista_json(datos, nombreJson):
    with open(nombreJson, "w", encoding="utf-8") as archivo:
        try:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
            print(f"\nArchivo creado exitosamente. Ruta: {os.path.abspath(nombreJson)}")
            time.sleep(1)
        except Exception as e:
            print(f"No se ha podido crear el archivo: {e}")
            time.sleep(1)