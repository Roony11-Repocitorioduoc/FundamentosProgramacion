nombreUsuario=input("Ingresa tu nombre: \n")

pesoUsuario=int(input("Ingresa tu peso: \n"))

estaturaUsuario=int(input("Ingresa tu estatura: \n"))

imc=pesoUsuario/(estaturaUsuario)^2

if (imc < 18.5):
    CLASIFICACION="BAJO PESO"
elif (imc < 24.9):
    CLASIFICACION="NORMAL"
elif (imc < 29.9):
    CLASIFICACION="SOBREPESO"
else:
    CLASIFICACION="OBESIDAD"
    
print(f"Usuario: {nombreUsuario}\nPeso: {pesoUsuario}\nEstatura: {estaturaUsuario}\n IMC: {imc}. Su clasificacion es: {CLASIFICACION}")