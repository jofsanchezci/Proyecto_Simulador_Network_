import time

class Enlace:
    def __init__(self, nodo_origen, nodo_destino, bw_mbps=100, delay_ms=2):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.bw = bw_mbps * 1_000_000  # bps
        self.delay = delay_ms / 1000   # segundos

    def transmitir(self, emisor, datos):
        tamanio_bits = len(datos) * 8
        t_tx = tamanio_bits / self.bw
        print(f"[Enlace] Transmitiendo {tamanio_bits} bits...")
        print(f"[Enlace] Tiempo de transmisión: {t_tx*1000:.2f} ms")
        print(f"[Enlace] Tiempo de propagación: {self.delay*1000:.2f} ms")
        time.sleep(t_tx + self.delay)
        self.nodo_destino.recibir(datos)