import socket as sk

puerto = 23000
sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
#"127.0.0.1" esta ip es para dirigirte a ti mismo
sock.bind(("127.0.0.1", 23000)) #El socket es una dupla entre ip y puerto

print(f"Este script recibe peticiones UDP en el puerto {puerto}")

while True:
    datos, direccion = sock.recvfrom(1024)
    print(f"De la direccion: {direccion} llega la siguiente informacion: \n "
          f"{datos.decode()}")