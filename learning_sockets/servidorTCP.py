import socket as sk
import pickle

puerto =25000
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
sock.bind(("127.0.0.1", puerto))

sock.listen(1)

print("El servidor esta escuchando...")

sock.accept()
connexion, direccion = sock.accept()
print(f"Conectado con {direccion}")

salir = False
while not salir:
    datos = connexion.recv(1024)
    if not datos:
        salir = True
        print("Se corto la conexion.")
    print(f"Llega la siguiente informacion: \n"
          f"{pickle.loads(datos)}")

connexion.close()