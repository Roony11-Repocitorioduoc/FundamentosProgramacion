import os
import time

# Variables

nota_1, nota_2, nota_3 = 0, 0, 0 # Variable guarda notas
promedio = 0 # variable promedio
estado = "" # string estado
cantidad_aprobado = 0 # cantidad de aprobados
cantidad_reprobado = 0 # cantidad de reprobados

menuprincipal_seleccion = "" # string seleccion menu principal

# Main

while True:
    while True:
        os.system("cls")
        print("""1.- Calcular Promedio
2.- Ver Resultado Estadisticas
3.- Salir\n
""")
        menuprincipal_seleccion = input("Ingresa tu seleccion\n")
        
        if (menuprincipal_seleccion.isdigit()):
            menuprincipal_seleccion=int(menuprincipal_seleccion)
            if (1<=menuprincipal_seleccion<=3):
                break
            else:
                print("Debes elegir una de las opciones del menu")
                time.sleep(1)
        else:
            print("Ingresa un digito!")
            time.sleep(1)
    
    if (menuprincipal_seleccion==1):
        print("Menu Calculador de Promedios\n")
        
        while True:
           os.system("cls")
           try:
               nota_1 = float(input("Ingresa la nota 1\n"))
           except(ValueError):
               print("Ingresa un entero o decimal!")
               time.sleep(1)
           if ((nota_1<1) or (nota_1>7)):
               print("La nota debe ser entre [1,7]")
           else:
               break
        while True:
            os.system("cls")
            try:
               nota_2 = float(input("Ingresa la nota 2\n"))
            except(ValueError):
               print("Ingresa un entero o decimal!")
               time.sleep(1)
            if ((nota_2<1) or (nota_2>7)):
               print("La nota debe ser entre [1,7]")
            else:
               break
        while True:
            os.system("cls")
            try:
               nota_3 = float(input("Ingresa la nota 3\n"))
            except(ValueError):
               print("Ingresa un entero o decimal!")
               time.sleep(1)
            if ((nota_3<1) or (nota_3>7)):
                print("La nota debe ser entre [1,7]")
                time.sleep(1)
            else:
                break
        
        promedio=(nota_1+nota_2+nota_3)/3
        
        if (promedio>4):
            estado = "APROBADO"
            cantidad_aprobado+=1
        else:
            estado = "REPROBADO"
            cantidad_reprobado+=1
            
        print(f"""*** Reporte ***
Nota 1: {nota_1}
Nota 2: {nota_2}
Nota 3: {nota_3}

Promedio: {promedio}
Estado: {estado}\n
""")
        
        
        input("Preciona ENTER para continuar")
    elif (menuprincipal_seleccion==2):
        print("Menu de Estadisticas\n")
        if ((cantidad_reprobado+cantidad_aprobado)==0):
            print("Debes ingresar los datos de almenos un estudiante!")
        else:
            print(f"""Cantidad de estudiantes atendidos: {cantidad_aprobado+cantidad_reprobado}
Cantidad de estudiantes aprobrados: {cantidad_aprobado}
Cantidad de estudiantes reprobados: {cantidad_reprobado}
""")
        
        input("Preciona ENTER para continuar")
    else:
        print("Saliendo...")
        break