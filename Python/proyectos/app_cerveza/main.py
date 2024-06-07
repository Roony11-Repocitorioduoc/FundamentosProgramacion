import validar
import os

estilo = ["Frutal", "Ale", "Amber"]

lista_cerveza = []

control = 0

while control!=4:
    os.system("cls")
    control = int(input(f"1. Agregar cerveza\n2. Ver cervezas\n3. Buscar Cerveza por codigo\n4. Salir"))
    if (control==1):
        lista_cerveza.append(validar.cerveza(estilo))
    elif (control==2):
        validar.lista(lista_cerveza)
    elif control==3:
        validar.codigo(lista_cerveza)


