nombreUsuario=input("Ingresa tu nombre: \n")

pesoUsuario=int(input("Ingresa tu peso: \n"))

estaturaUsuario=float(input("Ingresa tu estatura: \n"))

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

# git config --global user.email "rica.sanchezs@duocuc.cl"
# git config --global user.name "Roony11"
# git commit -m "Mensaje"