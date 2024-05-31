import os 
import time

def entero(texto):
    while True:
        try:
            variableentera = int(input(texto))
            return variableentera
        except:
            print("Ingresa un número entero!\n")
            time.sleep(1)

def decimal(texto):
    while True:
        try:
            variabledecimal = float(input(texto))
            return variabledecimal
        except:
            print("Ingresa un número real!\n")
            time.sleep(1)

def matriz(cantidad_filas, cantidad_columnas):
    matriz_resultante = []
    print(f"Ingrese la matriz {cantidad_filas}x{cantidad_columnas}")
    for i in range(cantidad_filas):
        fila = []
        for k in range(cantidad_columnas):
            valor = decimal(f"Ingrese el valor de la casilla {i+1},{k+1}: ")
            fila.append(valor)
        matriz_resultante.append(fila)
    return matriz_resultante

def suma_matriz(matriz1, matriz2):
    columnas = len(matriz1[0])
    filas = len(matriz1)
    matriz_resultado = []

    for i in range(filas):
        fila = []
        for k in range(columnas):
            fila.append(matriz1[i][k]+matriz2[i][k])
        matriz_resultado.append(fila)
    return matriz_resultado

def ponderacion_matriz(escalar, matriz):
    columnas = len(matriz[0])
    filas = len(matriz)
    matriz_resultado = []

    for i in range(filas):
        fila = []
        for k in range(columnas):
            fila.append(matriz[i][k]*escalar)
        matriz_resultado.append(fila)
    return matriz_resultado

