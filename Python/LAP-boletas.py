import time
import os

def esperar_tecla(segundos):
    time.sleep(segundos)
    input("Preciona ENTER para continuar") 

# deberia ingresar nombre, sexo, edad, valor hora, horas trabajadas. Como datos de usuario
# Usuario(nombre, sexo, edad, valor hora, horas trabajaras)

# guardar estos datos para luego printear algo por este estilo
# +-   Tipo        -+-           Haberes           -+-           Descuentos             -+
# | Sueldo bruto    | (valor_hora*horas_trabajadas) |                                    |
# +-----------------+-------------------------------+------------------------------------+
# | Salud(7%)       |                               | (valor_hora*horas_trabajadas)*0.07 |
# +-----------------+-------------------------------+------------------------------------+
# | Pensión(13%)    |                               | (valor_hora*horas_trabajadas)*0.13 |
# +-----------------+-------------------------------+------------------------------------+
# +**************************************************************************************+
# + Liquido a pagar: (valor_hora*horas_trabajadas)(1-0.2)=t*0.8 +
# +-------------------------------------------------------------+
# + Sexo: (H/M), Edad: edad, Tiempo a jubilacion: edadjubi-edad

# Ingresemos los datos del usuario
# Nombre
nombre = input("Ingresa el nombre.\n")
# Sexo
while True:
    sexo = input("Ingresa tu sexo (H/M)\n")
    
    if ((sexo=="h") or (sexo=="H") or (sexo=="m") or (sexo=="M")):
        break
    else:
        print("Ingresa una opción valida!")
        esperar_tecla(1)

# Edad
while True:
    edad = input("Ingresa tu edad.\n")

    if (edad.isdigit()):
        edad_entera = int(edad)
        break
    else:
        print("Ingresa números enteros.\n")
        esperar_tecla(1)

# Valor hora
while True:
    try:
        valor_hora=float(input("Ingresa el valor de hora trabajada.\n"))
        break
    except ValueError:
        print("Ingresa un valor valido!\n")
        esperar_tecla(1)

# Horas trabajadas al mes
while True:
    try:
        horas_trabajadas=float(input("Ingresa la cantidad de horas trabajadas este mes.\n"))
        break
    except ValueError:
        print("Ingresa un valor valido!\n")
        esperar_tecla(1)
    
    
    

os.system("cls")

print(f''' ** Liquidación de: {nombre} **
 +-   Tipo        -+-           Haberes           -+-           Descuentos             -+
 | Sueldo bruto    | {valor_hora*horas_trabajadas} |                                    |
 +-----------------+-------------------------------+------------------------------------+
 | Salud(7%)       |                               | {valor_hora*horas_trabajadas*0.07} |
 +-----------------+-------------------------------+------------------------------------+
 | Pensión(13%)    |                               | {valor_hora*horas_trabajadas*0.13} |
 +-----------------+-------------------------------+------------------------------------+
 +**************************************************************************************+
 + Liquido a pagar: {(valor_hora*horas_trabajadas)*(0.8)}
 +-------------------------------------------------------------+
        ''')
if (sexo=="H" or sexo=="h"):
    jubilacion=65-edad_entera
    print(f"+ Sexo: {sexo}, Edad: {edad}, Tiempo a jubilacion: {jubilacion}")
elif (sexo=="M" or sexo=="m"):
    jubilacion=60-edad_entera
    print(f"+ Sexo: {sexo}, Edad: {edad}, Tiempo a jubilacion: {jubilacion}")
