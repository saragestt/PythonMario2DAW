#Generar aleatoriamente un numero del 1 al 100
#El usuario tiene que adivinarlo
#Dar pistas: mas alto o mas bajo
#Muy caliente: menos de 5
#Caliente: menos de 15
# muy Frio: mas de 25
#Frio: mas de 50

import random


numero = random.randint(1,100)
print(numero)
introduce = int(input("Introduce un numero: "))
resultado = numero - introduce
absoluto = abs(resultado)
print(absoluto)

while numero != introduce:
    if absoluto >=1 and absoluto <= 5:
        print("Muy caliente")
    elif absoluto >=6 and absoluto <= 15:
        print("Caliente")
    elif absoluto >=16 and absoluto <= 25:
        print("Frio")
    elif absoluto >=26 and absoluto <= 50:
        print("Muy frio")
    else:
        print("Helado")

    introduce = int(input("Introduce un numero: "))
    resultado = numero - introduce
    absoluto = abs(resultado)


print("Has acertado")
