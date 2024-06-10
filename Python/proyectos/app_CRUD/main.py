# Datos a guardar en CRUD { Estudiante: - RUN - NOMBRE - CARRERA - JORNADA}

import imprimir
import estudiante

# Lista estudiantes
lista_estudiantes = []

# Menú principal
menu_principal = ["Crear Estudiante", "Listar Estudiante", "Actualizar Estudiante", "Borrar Estudiante"]

# Control menú
control = 0

while True:
    control = imprimir.menu(menu_principal, True)
    
    if control==1:
        lista_estudiantes.append(estudiante.añadir())
    elif control==2:
        estudiante.listar(lista_estudiantes)
    elif control==3:
        estudiante.actualizar(lista_estudiantes)
    elif control==len(menu_principal)+1:
        break