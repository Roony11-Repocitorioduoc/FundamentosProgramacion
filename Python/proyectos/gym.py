import os
import time

# Listas 
nombres = []
edades = []
pesos = []
estaturas = []
imc_usuarios = []
clasificacion_usuarios = []
# Variables
edadminima = 0
index = 0
## Usuarios
nombre = ""
nombre_old = ""
edad = 0
edad_old = 0
peso = 0.0
estatura = 0.0
## Menús
control_principal = 0
control_modificacion = 0
# Strings
## Textos a usuario
mensaje_valueerror = "ERROR, Ingresa un número entero"
mensaje_outindex = "ERROR, Ingresa un número entre las opciones del menú"
## Menú principal
menu_principal = f"""Menú principal
Selecciona la accion que deseas ejecutar a continuación (1-5)
1. Ingresar usuario
2. Modificar usuario
3. Borrar usuario
4. Ver estadísticas
5. Salir

Ingresa tu opción:
"""

menu_modificacion = f"""Modificar usuario
Selecciona que aspecto deseas modificar (1-5)
1. Nombre
2. Edad
3. Peso
4. Estatura
5. Salir

Ingresa tu opción
"""
# Main
while True:
    while True:
        try:
            os.system("cls")
            control_principal = int(input(menu_principal))
            
            if (1<=control_principal<=5):
                break
            else:
                print(mensaje_outindex)
                time.sleep(1)
        except:
            print(mensaje_valueerror)
            time.sleep(1)
    
    if (control_principal==1):
        os.system("cls")
        while True:
            nombre = str(input(f"Ingresa el nombre del usuario\n")).lower().strip()
            if (len(nombre)>0):
                if (nombres.count(nombre)==0):
                    break
                else:
                    print("ERROR, Ya existe este usuario!")
            else:
                print("Ingresa un nombre valido!")
         
        while True:
            try:
                edad = int(input(f"Ingresa la edad del usuario\n"))
                if (edad>edadminima):
                    break
                else:
                    print("ERROR, Ingresa una edad valida!")
            except:
                print(mensaje_valueerror)
                time.sleep(1)
        
        while True:
            try:
                peso = float(input(f"Ingresa el peso del usuario(Kilogramos)\n"))
                if (peso>0):
                    break
                else:
                    print("ERROR, Ingresa un peso valido!")
            except:
                print(mensaje_valueerror)
                time.sleep(1)
                
        while True:
            try:
                estatura = float(input(f"Ingresa la estatura del usuario(Metros)\n"))
                if (estatura>0):
                    break
                else:
                    print("ERROR, Ingresa una estatura valida!")
            except:
                print(mensaje_valueerror)
                time.sleep(1)
                
        
                
        nombres.append(nombre)
        edades.append(edad)
        pesos.append(peso)
        estaturas.append(estatura)
        imc_usuarios.append(round((peso/estatura**2)))
        
        input(f"Usuario {nombre} ingresado correctamente\nPresiona ENTER para continuar")
    elif (control_principal==2): # Hacer que el menu se actualice en tiempo real! dejo como pendiente ya no quiero hacer mas
        control_modificacion=0
        os.system("cls")
        
        nombre = str(input(f"Ingresa el nombre del usuario\n")).lower().strip()
        
        while True:  
            if (nombres.count(nombre)>0):
                index = nombres.index(nombre)
                nombre_old = nombre
            else:
                print("ERROR, Este usuario no existe!")
                time.sleep(1)
                break
                
        
            try:
                os.system("cls")
                control_modificacion = int(input(menu_modificacion))
            
                if (1<=control_modificacion<=5):
                    break
                else:
                    print(mensaje_outindex)
                    time.sleep(1)
            except:
                print(mensaje_valueerror)
                time.sleep(1)
            
            
        if (control_modificacion==1):
            os.system("cls")
            nombre = str(input(f"Ingresa el nombre que deseas colocarle al usuario\n")).lower().strip()
            
            if (nombres.count(nombre)>0):
                print("ERROR, Ya existe ese usuario!")
                time.sleep(1)
            else:
                # Cambio de nombre
                nombres.pop(index)
                nombres.insert(index, nombre)
                print(f"El usuario {nombre_old} se a cambiado satisfactoriamente a {nombre}")
                time.sleep(1)    
        elif (control_modificacion==2):
            os.system("cls")
            
            edad_old = edades[index]
            
            while True:
                try:
                    edad = int(input(f"Ingresa la edad que deseas colocarle al usuario\n"))
                    
                    if (edad>0):
                        break
                    else:
                        print("Ingresa una edad valida")
                        time.sleep(1)
                except:
                    print(mensaje_valueerror)
                    time.sleep(1)
            
            
            # Cambio de nombre
            edades.pop(index)
            edades.insert(index, edad)
            print(f"La edad {edad_old} se a cambiado satisfactoriamente a {edad}")
            time.sleep(1)        
        
        
    elif (control_principal==3):
        print("En construcción")
    elif (control_principal==4):
        print(nombres)
        print(edades)
        print(pesos)
        print(estaturas)
        
        input(f"\nENTER para continuar")
    elif (control_principal==5):
        break