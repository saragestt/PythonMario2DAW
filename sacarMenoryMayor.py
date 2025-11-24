# Genera una lista con n elementos aleatorios(n lo introduce el usuario, pero como minimo 5 y maximo 1000)
# que recorramos para extraer el menor y el mayor numero
import random

def getLongitudLista(min,max):
    numero = int(input("Introduce un numero entre el 5 y 1000: "))
    while (numero < min and max > 1000):
        numero = int(input("Introduce un numero entre el 5 y 1000: "))
    return numero

def sacarMinMiax(lista):
    min = 0
    max = 0
    for numero in lista:
        if numero < min:
            min = numero

        if numero > max:
            max = numero
    return (min,max)





