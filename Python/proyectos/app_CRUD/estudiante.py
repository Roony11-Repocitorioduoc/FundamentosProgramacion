import os
import time
import imprimir
import validar

def añadir():
    os.system("cls")
    
    run = str(input(f"Ingresa el RUN del estudiante:\n"))
    nombre = str(input(f"Ingresa el Nombre del estudiante:\n"))
    carrera = str(input(f"Ingresa la Carrera del estudiante:\n"))
    jornada = str(input(f"Ingresa la Jornada del estudiante:\n"))
    
    estudiante = {
        "run": run.lower().strip(),
        "nombre": nombre.lower().strip(),
        "carrera": carrera.lower().strip(),
        "jornada": jornada.lower().strip()
    }
    
    return estudiante

def listar(lista_estudiantes):
    os.system("cls")
    
    if (len(lista_estudiantes)==0):
        print(f"No hay estudiantes que mostrar!")
        time.sleep(1)
        return 0
    
    print(f"Imprimiremos en pantalla a los estudiantes y crearemos un archivo con los datos en ellos")
    time.sleep(1)
    
    os.system("cls")
    c = 1
    for i in range(len(lista_estudiantes)):
        print(f"""Estudiante  número: {c}
Nombre: {lista_estudiantes[i]["nombre"]} - Run: {lista_estudiantes[i]["run"]}
Carrera: {lista_estudiantes[i]["carrera"]} - Jornada: {lista_estudiantes[i]["jornada"]}
""")
        c=c+1
        
    # Escribamos un json con los estudiantes
    imprimir.lista_json(lista_estudiantes, "datosEstudiantes.json")
    
    input(f"\nENTER\n")

def filtrar(lista_estudiantes):
    lista_atributos = [] # Guarda los atributos disponibles
    lista_atributo = [] # Guarda el atributo especificado de cada usuario
    lista_id = [] # Guarda las id de estudiantes con el mismo atributo
    c=1 # Usuario Número n filtrado
    cantidad_estudiantes = len(lista_estudiantes)

    for k in lista_estudiantes[0].keys(): # Llena la lista de los atributos disponibles
        lista_atributos.append(k) 

    imprimir.menu(lista_atributos, f"Selección de atributo para filtrar", False) # Imprime un menú con los atributos disponibles
    
    seleccion = validar.entero(f"Ingresa la opción del menú\n")
    # devuelve el indice de la lista+1 del atributo

    # Crearemos una lista con elementos unicos de cada usuario para filtrar más facilmente
    for i in range(cantidad_estudiantes): # Verificamos cada json almacenado en nuestra lista
        for k, v in lista_estudiantes[i].items():
            if k == lista_atributos[seleccion-1]:
                lista_atributo.append(v) # Guarda los datos
    
    lista_atributo = set(lista_atributo) # Quita redundancia
    lista_atributo = list(lista_atributo)

    imprimir.menu(lista_atributo, f"Selecciona el atributo a filtrar", False)

    usuarios = validar.entero(f"Ingresa la opción del menú\n")

    os.system("cls")
    print(f"Filtrando por: {lista_atributos[seleccion-1]}")
    for i in range(len(lista_estudiantes)):
        if lista_estudiantes[i][lista_atributos[seleccion-1]]==lista_atributo[usuarios-1]:
            lista_id.append(i)
            print(f"""{c}.
Nombre: {lista_estudiantes[i]["nombre"]} - Run: {lista_estudiantes[i]["run"]}
Carrera: {lista_estudiantes[i]["carrera"]} - Jornada: {lista_estudiantes[i]["jornada"]}
""")
            c=c+1
    
    control = validar.entero(f"Selecciona el estudiante\n")

    return lista_estudiantes[lista_id[control-1]], lista_atributos # Devuelve el diccionario a modificar, atributos

def actualizar(lista_estudiantes):
    if (len(lista_estudiantes)==0):
        print(f"No hay estudiantes que mostrar!")
        time.sleep(1)
        return 0
    cambiar = 0
    # lista_estudiantes[lista_id[control-1]] Accedemos directamente al diccionario como el seleccionado!

    estudiante, lista_atributos = filtrar(lista_estudiantes)
    
    while True:
        os.system("cls")
        print(f"Ingresa que dato del usuario deseas cambiar\n")

        print(f"""Datos del estudiante:
1. Run: {estudiante["run"]}
2. Nombre: {estudiante["nombre"]}
3. Carrera: {estudiante["carrera"]}
4. Jornada: {estudiante["jornada"]}
5. Guardar
""")
        
        cambiar = validar.entero(f"Selecciona lo que deseas cambiar\n")


        if 1<=cambiar<=len(lista_atributos):
            validar.cambio(lista_atributos, estudiante, cambiar)
        elif cambiar==len(lista_atributos)+1:
            break

def borrar(lista_estudiantes):
    if (len(lista_estudiantes)==0):
        print(f"No hay estudiantes que mostrar!")
        time.sleep(1)
        return 0
    # lista_estudiantes[lista_id[control-1]] Accedemos directamente al diccionario como el seleccionado!

    estudiante, lista_atributos = filtrar(lista_estudiantes)

    lista_estudiantes.pop(lista_estudiantes.index(estudiante)) # lo borra
            
            
        
        
    
    
    
    
            
        
    
        
        
    
        
        
    
    
    
    