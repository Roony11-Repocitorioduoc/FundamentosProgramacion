import os

def entero(title):
    while True:
        try:
            variableentera = int(input(title))
            return variableentera
        except Exception as e:
            print("Error: ", e)
            os.system("pause")
