import menu
import notas

# Listas de menú
menu_principal = ["Ingresar Nota", "Ver notas", "Calcular promedio", "holaa"]
menu_hola = ["Hola", "Adios"]
# Lista de nota
lista_notas = []
# Variable de control
control = 0
control_principal = 0
control_hola = 0

while True:
    control_principal = menu.mostrar(control, menu_principal)
    
    if (control_principal==0):
        break
    elif (control_principal==1):
       notas.cargar(lista_notas)
    elif (control_principal==2):
        print(lista_notas)
        
        input("ENTER")
    elif (control_principal==3):
        notas.promedio(lista_notas)
        
        input("ENTER")
    elif (control_principal==4):
        control_hola = menu.mostrar(control, menu_hola)
        
    
    
    
    