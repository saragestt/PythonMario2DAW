
#Genera un cuadrado de nxn introducido por el usuario y lleno de 0 en utilidad
filas = int(input("Ingresa las filas: "))
columnas = int(input("Ingresa las columnas: "))

#matriz = []
#
#for i in range(filas):
#    matriz.append([])
#    for j in range(columnas):
#        matriz[i].append(0)
#
#
#
#for fila in matriz:
#    print(fila)



#Coger ese programa y llenar de 1 la diagonal
#cuadrado = []
#for i in range(filas):
#    cuadrado.append([])
#    for j in range(columnas):
#        if i == j:
#            cuadrado[i].append(1)
#        else:
#            cuadrado[i].append(0)
#
#for fila in cuadrado:
#    print(fila)

#Coger ese programa y llenar de 1 la diagonal a la inversa

cuadradoInverso = []


for i in range(filas):
    cuadradoInverso.append([])
    for j in range(columnas):
        if i + j == columnas -1:
            cuadradoInverso[i].append(1)
        else:
            cuadradoInverso[i].append(0)



for fila in cuadradoInverso:
    print (fila)
