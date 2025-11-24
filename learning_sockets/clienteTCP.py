import pickle
import socket as sk
import time

puerto = 25000
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

sock.connect(("127.0.0.1", puerto))

salir = False
while not salir:
    #mensaje = input("Introduce tu mensaje: ")
    mensajeJSON = {"user": "profe", "msg":"suerte para el examen"}
    #sock.send(mensaje.encode())
    sock.send(pickle.dumps((mensajeJSON)))
    print("Mensaje enviado.")
    time.sleep(1)

    if mensajeJSON["msg"] == "salir":
        salir = True

