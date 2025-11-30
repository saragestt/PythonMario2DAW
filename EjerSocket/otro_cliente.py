import socket as sk


sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
puerto = 23001

salir = False
while not salir:
    mensaje = input("Introduce el mensaje a enviar o escribe salir: ")
    sock.sendto(mensaje.encode(), ("127.0.0.1", puerto))
    print("El mensaje se ha enviado")
    if mensaje == "salir":
        salir = True