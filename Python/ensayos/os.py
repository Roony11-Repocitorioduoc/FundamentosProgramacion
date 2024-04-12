import os
import time

# libreria os
os.system("cls")

nota_1 = float(input("Ingresa nota 1"))
nota_2 = float(input("Ingresa nota 2"))
nota_3 = float(input("Ingresa nota 3"))

promedio = (nota_1+nota_2+nota_3)/3

if (promedio>=4):
    estado = "aprobado"
else:
    estado = "reprobado"

print(f"Tu promedio es: {promedio}. Estas {estado}")

time.sleep(5)

os.system("cls")

print(f'''
      ========= reporte de notas ========
      Nota 1 : {nota_1}
      Nota 2 : {nota_2}
      Nota 3 : {nota_3}
      -------------------
      Promedio : {promedio}
      
      En este momento estás {estado}
      ''')