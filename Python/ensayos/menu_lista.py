# Printear un menu dinamico, que lea desde una lista

def mostrar_menu(nombres):
    print("Menú:")
    for i, nombres in enumerate(nombres, start=1):
        print(f"{i}. {nombre}")
    print("0. Salir")

def main():
    nombres = ["Juan", "María", "Pedro", "Ana", "perro"]

    while True:
        mostrar_menu(nombres)
        opcion = input("Seleccione un nombre (o 0 para salir): ")

        if opcion == '0':
            print("¡Adiós!")
            break
        elif opcion.isdigit():
            indice = int(opcion)
            if 1 <= indice <= len(nombres):
                print(f"Seleccionó: {nombres[indice - 1]}")
            else:
                print("¡Opción inválida! Por favor, seleccione un número válido.")
        else:
            print("¡Opción inválida! Por favor, ingrese un número.")

if __name__ == "__main__":
    main()
