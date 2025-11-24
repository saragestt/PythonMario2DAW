from turtledemo.paint import switchupdown

cuadradoMagico = [[16,2,3,13],
                  [5,11,10,8],
                  [9,7,6,12],
                  [4,14,15,1]]


def esMagico(matriz):
    sumaDia = 0
    sumaDiaInv = 0
    Columnas = []
    Filas = []
    for i in range(len(matriz)):
        sumColumnas = 0
        sumFilas = 0
        for j in range(len(matriz)):
            if i == j:
               sumaDia += matriz[i][j]
            if i+j==len(matriz)-1:
                sumaDiaInv += matriz[i][j]
            sumColumnas += matriz[j][i]
            sumFilas += matriz[i][j]
        Filas.append(sumFilas)
        Columnas.append(sumColumnas)
    print(f"La diagonal es: {sumaDia}\n")
    print(f"La diagonal inversa es: {sumaDiaInv}\n")
    print(f"La suma de las filas es: {Filas}\n")
    print(f"La suma de las columnas es: {Columnas}\n")
    if sumaDia == sumaDiaInv and Filas == Columnas:
        print("Es magico")
    else:
        print("No es magico")
esMagico(cuadradoMagico)