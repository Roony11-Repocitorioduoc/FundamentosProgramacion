# Datos a guardar en CRUD { Estudiante: - RUN - NOMBRE - CARRERA - JORNADA}

import imprimir
import estudiante
import validar

# Lista estudiantes
lista_estudiantes = []

# Menú principal
menu_principal = ["Crear Estudiante", "Listar Estudiante", "Actualizar Estudiante", "Borrar Estudiante"]

# Control menú
control = 0

estudiante1 =  {
    "run": "20923917-2",
    "nombre": "Ricardo Sánchez",
    "carrera": "Ing Informatica",
    "jornada": "Diurno"
}
estudiante2 =  {
    "run": "31122123-9",
    "nombre": "Jose Sánchez",
    "carrera": "Ing Informatica",
    "jornada": "Vespertino"
}
estudiante3 =  {
    "run": "12322173-9",
    "nombre": "Marco Sánchez",
    "carrera": "Ing Informatica",
    "jornada": "Noche"
}
estudiante4 =  {
    "run": "12222173-9",
    "nombre": "Harco Sánchez",
    "carrera": "Ing Informatica",
    "jornada": "Noche"
}
estudiante5 =  {
    "run": "223917-2",
    "nombre": "cardo Sánchez",
    "carrera": "Ing Informatica",
    "jornada": "Diurno"
}

lista_estudiantes.append(estudiante1)
lista_estudiantes.append(estudiante2)
lista_estudiantes.append(estudiante3)
lista_estudiantes.append(estudiante4)
lista_estudiantes.append(estudiante5)

while True:
    imprimir.menu(menu_principal, f"Menú principal", True)

    control = validar.entero(f"Selecciona porfavor\n")
    
    if control==1:
        lista_estudiantes.append(estudiante.añadir())
    elif control==2:
        estudiante.listar(lista_estudiantes)
    elif control==3:
        estudiante.actualizar(lista_estudiantes)
    elif control==4:
        estudiante.borrar(lista_estudiantes)
    elif control==len(menu_principal)+1:
        break