class Nodo:
    def __init__(self, id):
        self.id = id
        self.buffer = []

    def enviar(self, enlace, datos):
        print(f"[{self.id}] Enviando datos: {len(datos)} bits")
        enlace.transmitir(self, datos)

    def recibir(self, datos):
        print(f"[{self.id}] Datos recibidos: {len(datos)} bits")
        self.buffer.append(datos)