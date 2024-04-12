lista_caracteres = ["Nombre", "Sexo", "Edad", "Valor hora", "Horas trabajadas"]
matriz_datos = []

n_columnas = len(lista_caracteres)

while True:
    nueva_fila=[]

    for columna in range(n_columnas):
        if (len(matriz_datos)==0):
            nueva_fila.append(lista_caracteres[columna])
        else:
            if (columna<2):
                nueva_fila.append(input(f"Ingrese su {lista_caracteres[columna].lower()}"))
            else:
                nueva_fila.append(float(input(f"Ingrese su {lista_caracteres[columna].lower()}")))

    matriz_datos.append(nueva_fila)
    
    # Probemos la matriz
    for fila in matriz_datos:
        print(fila)

    input("Presiona ENTER para continuar")

    continuar = input("Desea continuar ingresando datos (S/N)")

    if continuar.lower() != "s":
        break