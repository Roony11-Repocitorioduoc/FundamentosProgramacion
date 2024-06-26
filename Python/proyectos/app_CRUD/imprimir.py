import os
import time
import json

def menu(menu, titulo, salir):
    os.system("cls")

    if len(menu)==0:
        print(f"No hay elementos que mostrar!")
        time.sleep(1)
        return 

    print(titulo)
    for i in range(len(menu)):
        print(f"{i+1}.- {menu[i]}")
        # Añade X.- Salir al final del menú segun requerimiento, salir = True (Aparece)
    if salir:
        print(f"{len(menu)+1}.- Salir")

def lista_json(datos, nombreJson):
    with open(nombreJson, "w", encoding="utf-8") as archivo:
        try:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
            print(f"\nArchivo creado exitosamente. Ruta: {os.path.abspath(nombreJson)}")
            time.sleep(1)
        except Exception as e:
            print(f"No se ha podido crear el archivo: {e}")
            time.sleep(1)