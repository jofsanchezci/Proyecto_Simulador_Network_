from core.nodo import Nodo
from core.enlace import Enlace

if __name__ == '__main__':
    n1 = Nodo("N1")
    n2 = Nodo("N2")

    enlace = Enlace(n1, n2, bw_mbps=100, delay_ms=2)

    # Simulación TCP: Handshake (simplificado)
    print("[TCP] Handshake iniciado")
    print("N1 → SYN → N2")
    print("N2 → SYN-ACK → N1")
    print("N1 → ACK → N2")

    # Envío de ráfaga de datos (1 MB)
    datos = "1" * (1024 * 1024)  # 1 MB en caracteres
    n1.enviar(enlace, datos)

    print("\n[FIN] Simulación completada.")