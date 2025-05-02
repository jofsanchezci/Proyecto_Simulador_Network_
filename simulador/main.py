import time
import random
import string
from core.nodo import Nodo
from core.enlace import Enlace

def obtener_tiempo_ejecucion():
    while True:
        try:
            tiempo_ejecucion = input("Ingrese el tiempo de ejecución de la simulación en segundos: ").strip()
            tiempo_ejecucion = float(tiempo_ejecucion)
            if tiempo_ejecucion <= 0:
                print("Por favor ingrese un número mayor que 0.")
            else:
                return tiempo_ejecucion
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar un número válido.")

def generar_datos_aleatorios(tamano):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=tamano))

if __name__ == '__main__':
    tiempo_ejecucion = obtener_tiempo_ejecucion()

    n1 = Nodo("N1")
    n2 = Nodo("N2")

    enlace = Enlace(n1, n2, bw_mbps=100, delay_ms=2)

    # Simulación TCP: Handshake (simplificado)
    print("[TCP] Handshake iniciado")
    print("N1 - SYN - N2")
    print("N2 - SYN-ACK - N1")
    print("N1 - ACK - N2")

    max_paquetes = int(tiempo_ejecucion * random.uniform(1.5, 3))
    num_paquetes = random.randint(int(tiempo_ejecucion), max_paquetes)

    for i in range(num_paquetes):
        tamano_aleatorio = random.randint(512 * 1024, 2 * 1024 * 1024)
        datos = generar_datos_aleatorios(tamano_aleatorio)

        tamanio_bits = len(datos) * 8
        print(f"\n[Simulación] Enviando paquete {i+1}/{num_paquetes}")
        print(f"[{n1.id}] Enviando datos: {tamanio_bits} bits")
        n1.enviar(enlace, datos)
        print(f"[Simulación] Paquete {i+1} enviado")
        tiempo_espera = random.uniform(0.5, 2)
        time.sleep(tiempo_espera)
        import sys
        sys.stdout.flush()

    print("\n[FIN] Simulación completada.")
