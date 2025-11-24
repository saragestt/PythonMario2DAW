import random


def esPar(numero):
    return numero % 2 == 0

def printMenu():
    print("¡Bienvenido a mi maquina xpendedora!")
    print("1. Seleccionar producto")
    print("2. Salir")

def dameUnNombre():
    lista = ["Lucia","Pedro"]
    return lista[random.randint(0,1)]


def printLowerNumber(listaN):
        min = listaN[0]
        for n in listaN:
            if n < min:
                min = n
        print(min)

printLowerNumber([0,1,2,34,3])
print(dameUnNombre())
printMenu()
print(esPar(5))