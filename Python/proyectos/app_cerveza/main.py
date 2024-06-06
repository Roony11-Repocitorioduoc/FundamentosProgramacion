import validar

estilo = ["Frutal", "Ale", "Amber"]

lista_cerveza = []

control = 0

while control!=3:
    control = int(input(f"1. Agregar cerveza\n2. Ver cervezas\n3. Salir"))
    if (control==1):
        lista_cerveza.append(validar.cerveza(estilo))
    elif (control==2):
        for cerveza in lista_cerveza:
            for k in cerveza.keys():
                print(f"{k} <-> {cerveza[k]}")
            print(f"---")

