import socket as sk
import time

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
puerto = 23000

salir = False
while not salir:
    mensaje = input("Introduce el mensaje a enviar o escribe salir: ")
    sock.sendto(mensaje.encode(), ("127.0.0.1", puerto))
    print("El mensaje se ha enviado")
    time.sleep(1)
    if mensaje == "salir":
        salir = True