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
    
def actualizar(lista_estudiantes):
    if (len(lista_estudiantes)==0):
        print(f"No hay estudiantes que mostrar!")
        time.sleep(1)
        return 0
    
    cambio = input(f"Ingresa el nombre del usuario a buscar\n")
    
    lista_id = [] # Guarda las id de estudiantes con el mismo nombre
    
    control = 0
    
    c=1
    
    for i in range(len(lista_estudiantes)):
        for k, v in lista_estudiantes[i].items(): # Datos Estudiante
            if lista_estudiantes[i]["nombre"]==cambio:
                lista_id.append(i) # Indice de la lista guardado
                print(f"{c}.- {k} --> {v}")
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
        print(f"{i+1}.- Salir")
        
        cambiar = validar.entero(f"Selecciona lo que deseas cambiar\n")
        
        if cambiar==1:
            # Run
            run = input(f"Ingresa el run a cambiar\n")
            
            
            lista_estudiantes[lista_id[control-1]]["run"] = run
        elif cambiar==5:
            break
            
            
        
        
    
    
    
    
            
        
    
        
        
    
        
        
    
    
    
    