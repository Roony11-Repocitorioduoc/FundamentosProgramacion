import menu
import validacion

# En este programa almacenaremos maximo dos matrices como maximo, donde desplegaremos 3 operaciones.

menu_principal = ["Suma de matrices", "Multiplicación de matrices", "Ponderación por escalar"]

# Matriz 1
matriz1 = []
# Matriz 2
matriz2 = []
#
matriz_resultante = []

# Matriz 1
cantidad_columnas1 = 0
cantidad_filas1 = 0
# Matriz 2
cantidad_columnas2 = 0
cantidad_filas2 = 0

control_menu = 0

# Bucle principal
while True:
    menu.crear("Menú principal", menu_principal, 1)

    control_menu = validacion.entero(f"Ingresa tu opción\n")

    if control_menu==0:
        break
    elif control_menu==1:
        cantidad_columnas1 = validacion.entero(f"Ingresa la cantidad de columnas de la matriz\n")
        cantidad_filas1 = validacion.entero(f"Ingresa la cantidad de filas de la matriz\n")

        # Ambas matrices iguales
        cantidad_columnas2 = cantidad_columnas1
        cantidad_filas2 = cantidad_filas1

        # Debemos ingresar los datos a las matrices uno a uno las coordenadas
        matriz1 = validacion.matriz(cantidad_filas1, cantidad_columnas1)
        matriz2 = validacion.matriz(cantidad_filas2, cantidad_columnas2)

        menu.matriz(matriz1)
        menu.matriz(matriz2)

        matriz_resultante = validacion.suma_matriz(matriz1, matriz2)

        menu.matriz(matriz_resultante)

        input("ENTER")
    elif control_menu==3:
        cantidad_columnas1 = validacion.entero(f"Ingresa la cantidad de columnas de la matriz\n")
        cantidad_filas1 = validacion.entero(f"Ingresa la cantidad de filas de la matriz\n")
        escalar = validacion.decimal(f"Ingresa el número decimal que multiplicara la matriz\n")

        matriz1 = validacion.matriz(cantidad_filas1, cantidad_columnas1)

        menu.matriz(matriz1)

        matriz_resultante = validacion.ponderacion_matriz(escalar, matriz1)

        menu.matriz(matriz_resultante)

        input("ENTER")
    else:
        print("Opción no valida!")
        input("ENTER")