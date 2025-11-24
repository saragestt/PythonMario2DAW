try: #el try prueba y en except te tira el error donde se puede personalizar
    int("a")
except ValueError:
    print("Has intentando castear a entero una letra")

class DormidoError(Exception):
    def __init__(self):
        self.message = "Error,esta dormido" #el self es como en java el this
        super().__init__(self.message)


despertarse = False
if (not despertarse):
    raise DormidoError

