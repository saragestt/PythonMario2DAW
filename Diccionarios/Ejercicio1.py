"""
funcion built-in de utilidad: clase <- type(valor) e isinstance(valor, clase)

1. Crea un programa que permita al usuario crear un diccionario custom. Permítele elegir el nombre de la clave,
el tipo de valor (str, int/float, list) y que llene ambas.

"""

nombre = input("Introduce el nombre de la clave:")
valor = input("Selecciona el valor(str, int/float, list):")

if valor == "str":
    nombre = str(nombre)
elif valor == "int" or valor == "float":
    nombre = int(nombre)
else:
    nombre = list(nombre)

print(type(nombre))

diccionario = {
    nombre : valor
}

for d in diccionario:
    print(diccionario[d])


def llenarArray(tipo):
    salir = False
    lista = []
    while not salir:
        print(tipo)
        if tipo is str:
            var = input("Introduce otro string o escribe 'salir':")
            if var == "salir":
                salir = True
            else:
                lista.append(var)
        elif tipo is int:
            try:
                var =int(input("Introduce otro int o escribe 'salir':"))
                if salir == "salir":
                    salir = True
                else:
                    lista.append(var)
            except ValueError:
                salir = True
    return lista

print(llenarArray(str))
print(llenarArray(int))
