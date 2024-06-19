import math


def estadisticas_basicas(valores_list):
    promedio = sum(valores_list)/len(valores_list)
    maximo = max(valores_list)
    minimo = min(valores_list)
    print(f'''Promedio: ${promedio}
Max       ${maximo}
Min       ${minimo}
          ''')
    
    
def media_geometrica(valores_list):
    # n será la cantidad de valores
    n = len(valores_list)

    # producto almacenará las multiplicaciones entre los valores
    producto = 1
    for valor in valores_list:
        producto *= valor

    # Media geométrica
    media_geometrica = producto ** (1/n)

    # Otra forma de definir la cantidad de decimales, en este caso 3 decimales
    print(f"La media geométrica de los valores {valores_list} es {media_geometrica:.3f}")
        