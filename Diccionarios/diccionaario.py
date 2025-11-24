import uuid

alumno = {
    "id": uuid.uuid4(),
    "nombre": ["Diana","Carolina","Pita"],
    "grado": "DAW",
    "curso":2,
    "asinaturas": ["Python", "DespAppWeb"],
    "tieneTrabajo": False,
    "material": {
        "portatil": uuid.uuid4(),
        "sobremesa": uuid.uuid4()
    }
}
#Acceder a distintod elementos metiendolos en una variable e imprimiendo todas al final
#ID, segundo nombre Diana, curso, asignaturas, array con las claves del material y el id de sobremesa
print(alumno)

id = alumno["id"]
s_nombre = alumno["nombre"][0]
curso = alumno["curso"]
asignaturas = alumno["asinaturas"]
for a in alumno["material"]:
    print(a)

print(alumno["material"]["sobremesa"])

