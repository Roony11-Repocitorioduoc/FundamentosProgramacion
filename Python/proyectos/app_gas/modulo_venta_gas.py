import os
import csv
import random

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def generar_valores_aleatorios(minimo, maximo):
    """genera un valor aleatorios en un rango
    """
    aleatorio = random.randrange(minimo, maximo)
    return aleatorio

def cargar_data_test():
    """Genera los datos para la BD en los 12 meses
    """
    
    lista_dict = []
    
    for k in range(len(meses)):
        valor = generar_valores_aleatorios(20000, 28000)
        cantidad = generar_valores_aleatorios(200, 300)
        
        dict = {
            "mes": meses[k],
            "valor_gas": valor,
            "cant_vendida": cantidad,
            "total_mes": valor*cantidad
        }
        
        lista_dict.append(dict)
    
    print("Datos cargados correctamente")
    return lista_dict

def listar_ventas_list(lista):
    """ Muestra los datos de una lista de json con las variables estadisticas del mes
    """
    if len(lista)==0:
        os.system("cls")
        print(f"No hay datos que mostrar")
        os.system("pause")
        return
    
    # Recorremos el diccionario
    os.system("cls")
    for k in range(len(lista)):
        # lista[k] es un diccionario
        print(f"""MES : {lista[k]["mes"]}
VALOR GAS : ${lista[k]["valor_gas"]}
CANTIDAD VENDIDA : {lista[k]["cant_vendida"]}
TOTAL MES : ${lista[k]["total_mes"]}
""")
    
    # creara una tabla que printeara todo
    return

def imprimir_csv(lista):
    cantidad = len(lista)
    if cantidad==0:
        os.system("cls")
        print(f"No hay datos que mostrar")
        os.system("pause")
        return
    
    archivo_reporte = "reporte_gas.csv"
    
    with open(archivo_reporte, "w", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Mes", "Valor Gas", "Cantidad Vendida", "Total Mes"])
        
        for k in range(cantidad):
            fila = [lista[k]["mes"], lista[k]["valor_gas"], lista[k]["cant_vendida"], lista[k]["total_mes"]]
            writer.writerow(fila)
        
        print(f"El reporte ha sido generado en: {os.path.abspath(archivo_reporte)}")