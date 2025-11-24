#Si es mayor de edad y esta aprbado => Aprobado
#Si es mayor de edad y esta aprobada => Aprobada
#Si es menor de edad y ha suspendido => No apto

nota  = int(input("Introduce tu nota:"))
edad = int(input("Introduce tu edad:"))
genero = input("Introduce tu genero(M/F):")

if nota >=5 and genero == "M" and edad >=18:
    print("Estas aprobado")
elif nota >=5 and genero == "F" and edad >=18:
    print("Estas aprobada")
else:
    print("No apto")