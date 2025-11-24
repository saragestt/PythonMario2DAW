"""
2. Haz el programa anterior escalable a un diccionario general con un nombre escogido por el usuario,
 por ejemplo "biblioteca" cuyo valor sea un array de diccionarios que tienen el sistema previo de
 introducción de información.
"""

nombre = input("Introduce el nombre del diccionario general: ")

diccionario_general = {nombre:[]}
seguir = True

while seguir == True:
    s = input("Quieres introducir un diccionario clave-valor?(s/n): ")
    if s == "s":
        diccionario_especifico = {}

        clave = input("Introduce el nombre de la clave: ")
        tipo = input("Introduce el tipo de valor(str,int/float, list): ")
        valor = input("Introduce el valor: ")

        if tipo == "str":
            valor = str(valor)
        elif tipo == "int":
            valor = int(valor)
        elif tipo == "float":
            valor = float(valor)
        elif tipo == "list":
            valor = valor.split(",")
        else:
            print("Error, tipo de valor no valido")

        diccionario_especifico[clave] = valor
        diccionario_general[nombre].append(diccionario_especifico)
    else:
        seguir = False



print(diccionario_general)