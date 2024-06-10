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
        "run": run,
        "nombre": nombre,
        "carrera": carrera,
        "jornada": jornada
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
    for i in range(len(lista_estudiantes)):
        # Cada estudinte en formato dict, lista_estudiantes[i] es un diccionario
        print(f"Estudiante registrado número {i+1}\n")
        for k, v in lista_estudiantes[i].items(): # Datos Estudiante
            print (f"{k} --> {v}")
        print(f"---")
        
    # Escribamos un json con los estudiantes
    imprimir.lista_json(lista_estudiantes, "datosEstudiantes.json")
    
    input(f"\nENTER\n")

def filtrar():
    print(f"Hola mundo!") # funcion que filtra por un atributo y devuelve diccionarios con esa caracteristica en común (posiblemente se puede agregar mas de uno proximamente)
    
def actualizar(lista_estudiantes):
    if (len(lista_estudiantes)==0):
        print(f"No hay estudiantes que mostrar!")
        time.sleep(1)
        return 0
    
    lista_id = [] # Guarda las id de estudiantes con el mismo nombre
    lista_atributos = [] # Guarda los atributos disponibles

    for k in lista_estudiantes[0].keys():
        lista_atributos.append(k)

    seleccion = imprimir.menu(lista_atributos, False)
    
    cambio = input(f"Ingresa el/la {lista_atributos[seleccion-1]} del usuario a buscar\n")
    
    control = 0
    
    c=1
    os.system("cls")
    for i in range(len(lista_estudiantes)):
        flagnumber = True
        for k, v in lista_estudiantes[i].items(): # Datos Estudiante
            if flagnumber:
                print(f"{c}.- ", end=" ")
            if lista_estudiantes[i][lista_atributos[seleccion-1]]==cambio:
                lista_id.append(i) # Indice de la lista guardado
                print(f"{k} --> {v}")
            flagnumber = False
        print(f"---")
        c=c+1
                
    control = validar.entero(f"Selecciona el usuario a modificar!\n")
    
    # lista_estudiantes[lista_id[control-1]] Accedemos directamente al diccionario como el seleccionado!
    
    while True:
        os.system("cls")
        print(f"Ingresa que dato del usuario deseas cambiar\n")
        
        i = 0
        for k, v in lista_estudiantes[lista_id[control-1]].items():
            print(f"{i+1}.- {k} --> Actual: {v}")
            i=i+1
        print(f"{i+1}.- Guardar")
        
        cambiar = validar.entero(f"Selecciona lo que deseas cambiar\n")

        if 1<=cambiar<=len(lista_atributos):
            validar.cambio(lista_atributos, lista_estudiantes[lista_id[control-1]], cambiar)
        elif cambiar==len(lista_atributos)+1:
            break
            
            
        
        
    
    
    
    
            
        
    
        
        
    
        
        
    
    
    
    