import os
import time

# Listas 
id_usuarios = []
nombres = []
edades = []
pesos = []
estaturas = []
imc_usuarios = []
clasificacion_usuarios = []
# Variables
edadminima = 0
index = 0
cantidad_usuarios = 0
## Usuarios
id = 0
nombre = ""
nombre_old = ""
edad = 0
edad_old = 0
peso = 0.0
peso_old = 0.0
estatura = 0.0
estatura_old = 0.0
imc = 0.0
categorizacion = ""
## Menús
control_principal = 0
control_modificacion = 0
control_estadisticas = 0
control_borrar = 0
# Strings
## Textos a usuario
mensaje_valueerror = "ERROR, Ingresa un número"
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

menu_estadistica = f"""Menú estadística
Selecciona la accion que deseas ejecutar a continuación (1-4)
1. Listar usuarios
2. Ver estadísticas del usuario
3. Estadísticas globales
4. Salir
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
                #if (nombres.count(nombre)==0):
                break
                #else:
                #    print("ERROR, Ya existe este usuario!")
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
                
        imc = peso/estatura**2
        
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
        
        # Carga de datos

        #if (len(id_usuarios)==0):
        #    id_usuarios.append(0)
        #else:
        id_usuarios.append(len(id_usuarios))

        nombres.append(nombre)
        edades.append(edad)
        pesos.append(peso)
        estaturas.append(estatura)
        imc_usuarios.append(round(imc))
        clasificacion_usuarios.append(categorizacion)
        
        input(f"Usuario {nombre} ingresado correctamente\nTu ID es {len(id_usuarios)-1}\nPresiona ENTER para continuar")
    elif (control_principal==2):
        control_modificacion=0
        os.system("cls")
        
        while True:
            os.system("cls")
            #nombre = str(input(f"Ingresa el nombre del usuario\n")).lower().strip()
            try:
                id = int(input(f"Ingresa el ID del usuario (0 - {len(id_usuarios)-1})\n"))
                if (id<=len(id_usuarios)):
                    index = id_usuarios.index(id)
                    break
                else:
                    print("ERROR, Ingresa una ID valido!")
            except:
                print(mensaje_valueerror)
                time.sleep(1) 

            #if (nombres.count(nombre)>0):
            #    index = nombres.index(nombre)
            #    nombre_old = nombre
            #    break
            #else:
            #    print("ERROR, Este usuario no existe!")
            #    time.sleep(1)     

        while True:
            while True: # bucle menú
                try:
                    os.system("cls")
                    control_modificacion = int(input(f"""Modificar usuario
    Selecciona que aspecto deseas modificar (1-5)
    ID: {id_usuarios[index]}
    1. Nombre [ACTUAL: {nombres[index]}]
    2. Edad [ACTUAL: {edades[index]}]
    3. Peso [ACTUAL: {pesos[index]}]
    4. Estatura [ACTUAL: {estaturas[index]}]
    5. Salir

    Ingresa tu opción
    """))
                
                    if (1<=control_modificacion<=5):
                        break
                    else:
                        print(mensaje_outindex)
                        time.sleep(1)
                except:
                    print(mensaje_valueerror)
                    time.sleep(1)
                
                
            if (control_modificacion==1): # cambio de nombre
                os.system("cls")
                nombre = str(input(f"Ingresa el nombre que deseas colocarle al usuario. ACTUAL: {nombres[index]}\n")).lower().strip()
                nombre_old = nombres[index]
                #if (nombres.count(nombre)>0):
                #    print("ERROR, Ya existe ese usuario!")
                #    time.sleep(1)
                #else:
                nombres.pop(index)
                nombres.insert(index, nombre)
                print(f"El usuario {nombre_old} se a cambiado satisfactoriamente a {nombre}")
                time.sleep(1)    
            elif (control_modificacion==2): # cambio de edad
                os.system("cls")
                
                edad_old = edades[index]
                
                while True:
                    try:
                        edad = int(input(f"Ingresa la edad que deseas colocarle al usuario. ACTUAL: {edades[index]}\n"))
                        
                        if (edad>0):
                            break
                        else:
                            print("Ingresa una edad valida")
                            time.sleep(1)
                    except:
                        print(mensaje_valueerror)
                        time.sleep(1)
                
                
                edades.pop(index)
                edades.insert(index, edad)
                print(f"La edad {edad_old} se a cambiado satisfactoriamente a {edad}")
                time.sleep(1)        
            elif (control_modificacion==3): # cambio de peso
                os.system("cls")
                
                peso_old = pesos[index]
                estatura_old = estaturas[index]
                
                while True:
                    try:
                        peso = float(input(f"Ingresa el peso que deseas colocarle al usuario. ACTUAL: {pesos[index]}\n"))
                        
                        if (peso>0):
                            break
                        else:
                            print("Ingresa un peso valida")
                            time.sleep(1)
                    except:
                        print(mensaje_valueerror)
                        time.sleep(1) 
                
                
                pesos.pop(index)
                pesos.insert(index, peso)
                
                imc = peso/estatura_old**2
                
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
                
                imc_usuarios.pop(index)
                imc_usuarios.insert(index, round(imc))
                
                clasificacion_usuarios.pop(index)
                clasificacion_usuarios.insert(index, categorizacion)
                
                print(f"El peso {peso_old} se a cambiado satisfactoriamente a {peso}")
                time.sleep(1) 
            
            elif (control_modificacion==4): # cambio de estatura
                os.system("cls")
                
                peso_old = pesos[index]
                estatura_old = estaturas[index]
                
                while True:
                    try:
                        estatura = float(input(f"Ingresa la estatura que deseas colocarle al usuario. ACTUAL: {estaturas[index]}\n"))
                        
                        if (estatura>0):
                            break
                        else:
                            print("Ingresa una estatura valida")
                            time.sleep(1)
                    except:
                        print(mensaje_valueerror)
                        time.sleep(1)
                
                
                estaturas.pop(index)
                estaturas.insert(index, estatura)
                
                imc = peso_old/estatura**2
                
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
                
                imc_usuarios.pop(index)
                imc_usuarios.insert(index, round(imc))
                
                clasificacion_usuarios.pop(index)
                clasificacion_usuarios.insert(index, categorizacion)
                
                print(f"La estatura {estatura_old} se a cambiado satisfactoriamente a {estatura}")
                time.sleep(1)

            elif (control_modificacion==5): # salir
                break

        input(f"\nENTER para continuar")
    elif (control_principal==3): # Borrar usuario
        while True:
            os.system("cls")
            #nombre = str(input(f"Ingresa el nombre del usuario\n")).lower().strip()
            try:
                id = int(input(f"Ingresa el ID del usuario (0 - {len(id_usuarios)})\n"))
                if (id<=len(id_usuarios)):
                    index = id_usuarios.index(id)
                    break
                else:
                    print("ERROR, Ingresa una ID valido!")
            except:
                print(mensaje_valueerror)
                time.sleep(1) 
        
        while True:
            try:
                os.system("cls")
                control_borrar = int(input(f"""Menú borrar usuario
Desea borrar al usuario {nombres[index]} ID: {id_usuarios[index]} (1-2)
1. Si
2. No
"""))
                if (1<=control_borrar<=2):
                    break
                else:
                    print(mensaje_outindex)
                    time.sleep(1)
            except:
                print(mensaje_valueerror)
                time.sleep(1)
        
        if (control_borrar==1):
            nombre_old = nombres[index]


            id_usuarios.pop(index)
            nombres.pop(index)
            edades.pop(index)
            pesos.pop(index)
            estaturas.pop(index)
            imc_usuarios.pop(index)
            clasificacion_usuarios.pop(index)

            for index in range(len(id_usuarios)):
                id_usuarios[index] -= 1

            print(f"Se ha eliminado exitosamente el usuario {nombre_old}")
        else:
            print(f"No se eliminara el usuario {nombre_old}")
            
        input(f"\nENTER para continuar")
    elif (control_principal==4):
        cantidad_usuarios = len(nombres)
        if cantidad_usuarios>0:
            while True:
                try:
                    os.system("cls")
                    control_estadisticas = int(input(menu_estadistica))
                    if (1<=control_estadisticas<=4):
                        break
                    else:
                        print(mensaje_outindex)
                        time.sleep(1)
                except:
                    print(mensaje_valueerror)
                    time.sleep(1)
            

            if (control_estadisticas==1): # Listar usuarios
                cantidad_usuarios = len(nombres)
                if cantidad_usuarios>0:
                    os.system("cls")
                    for usuario in range(cantidad_usuarios):
                        print(f"ID: {usuario} - USUARIO: {nombres[usuario]}")
                else:
                    print("No hay usuarios registrados!")

            elif (control_estadisticas==2): # Ver estadísticas de un usuario
                while True:
                    #nombre = str(input(f"Ingresa el nombre del usuario\n")).lower().strip()
                    try:
                        id = int(input(f"Ingresa el ID del usuario (0 - {len(id_usuarios)}\n"))
                        if (id<=len(id_usuarios)):
                            index = id_usuarios.index(id)
                            break
                        else:
                            print("ERROR, Ingresa una ID valido!")
                    except:
                        print(mensaje_valueerror)
                        time.sleep(1)  
                        
                os.system("cls")
                print(f"""|---------------------------------------------------------------------------|
Usuario: {nombres[index]} - ID: {id_usuarios[index]}
Edad: {edades[index]} - Peso: {pesos[index]} - Altura: {estaturas[index]}
IMC: {imc_usuarios[index]} - Categorización: {clasificacion_usuarios[index]}
|---------------------------------------------------------------------------|
""")
            elif (control_estadisticas==3): # Estadísticas promedio de todos los usuarios
                imc_promedio = sum(imc_usuarios)/cantidad_usuarios

                if imc_promedio<16:
                    categorizacion_promedio="Infrapeso: Delgadez severa"
                elif 16<=imc_promedio<17:
                    categorizacion_promedio="Infrapeso: Delgadez moderada"
                elif 17<=imc_promedio<18.5:
                    categorizacion_promedio="Infrapeso: Delgadez aceptable"
                elif 18.5<=imc_promedio<25:
                    categorizacion_promedio="Peso nomral"
                elif 25<=imc_promedio<30:
                    categorizacion_promedio="Sobrepeso"
                elif 30<=imc_promedio<35:
                    categorizacion_promedio="Obeso: Tipo I"
                elif 35<=imc_promedio<40:
                    categorizacion_promedio="Obeso: Tipo II"
                elif 40<=imc_promedio:
                    categorizacion_promedio="Obeso: Tipo III"
                
                os.system("cls")

                print(f"""Estadísticas de los usuarios en promedio
Edad promedio: {(sum(edades))/cantidad_usuarios} - Peso promedio: {(sum(pesos))/cantidad_usuarios} - Altura promedio: {(sum(estaturas))/cantidad_usuarios}
IMC promedio: {round(imc_promedio)} - Categorización promedio: {categorizacion_promedio}
""")         
        else:
            print("ERROR! No hay usuarios registrados")
            time.sleep(1)

        input(f"\nENTER para continuar")
    elif (control_principal==5):
        break