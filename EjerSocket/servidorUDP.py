import socket as sk
import random



puerto = 23001
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
#"127.0.0.1" esta ip es para dirigirte a ti mismo
sock.bind(("127.0.0.1", 23001)) #El socket es una dupla entre ip y puerto

print(f"Este script recibe peticiones UDP en el puerto {puerto}")


lista = ["Papayón", "miEnormeMelocotón", "Mangote", "Bananita", "Fresota","Kiwito"]
conectados = {}
malasPalabras = ["gilipollas", "estupido", "mierda", "puta"]

salir = False
while salir == False:

    datos, direccion = sock.recvfrom(1024)

    if direccion not in conectados:
        usuario = random.choice(lista)
        conectados[direccion] = usuario
        lista.remove(usuario)

        print(f"{usuario} ha entrado al chat.")
        print(f"{usuario}:\n"
              f"{datos.decode()}")

    else:
        for c in conectados:
            if direccion[1] == c[1]:

                if datos.decode() == "salir":
                    print(f"{usuario} ha dejado el chat.")

                else:

                    if datos.decode() in malasPalabras:
                        print(f"{usuario}:\n"
                              f"mensaje baneado")
                    else:
                        print(f"{usuario}:\n"
                           f"{datos.decode()}")













