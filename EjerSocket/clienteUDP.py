"""
Crea un chat con un script que funcione como servidor y otro como cliente.

En el lado servidor se les dará un nombre aleatorio de una lista predefinida. Dos clientes no pueden compartir el mismo nombre mientras estén conectados.
A partir de aquí se enviarán mensajes estilo chat online y se imprimirán en el servidor con estilo:
Fresa:
¡Hola a todxs!
Manzana:
Buenasss :D
 Cuando alguien entre o salga del servidor se mostrará el nombre del que se ha unido o del que ha salido del servidor.
Se filtrarán palabras malsonantes, ya sea baneando el mensaje o mostrando asteriscos en lugar de la palabra.

"""
import socket as sk
import time

sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
puerto = 23001

salir = False
while not salir:
    mensaje = input("Introduce el mensaje a enviar o escribe salir: ")
    sock.sendto(mensaje.encode(), ("127.0.0.1", puerto))
    print("El mensaje se ha enviado")

    if mensaje == "salir":

        salir = True