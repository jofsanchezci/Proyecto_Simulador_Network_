# Simulador de redes Ad Hoc en Python

**Proyecto académico - Opción de Grado II**  
**Corporación Universitaria Iberoamericana – Ingeniería de Software**  
**Bogotá D.C., 2025**


## 🧠 Descripción General

    Este repositorio contiene una implementación de un **simulador de conexiones TCP punto a punto**. El simulador modela el comportamiento de nodos conectados por un enlace lógico, simulando los procesos fundamentales del **protocolo TCP**, incluyendo:

    - Establecimiento de conexión (**Three-Way Handshake**)
    - Transmisión de ráfagas de datos
    - Cálculo de tiempos de transmisión y propagación
    - Métricas de desempeño

    Su arquitectura permite ampliar funcionalidades como nuevos protocolos, topologías, pérdida de paquetes o múltiples nodos.

## 📂 Estructura del Proyecto

    Proyecto_Simulador_Network_/
    ├── core/
    │   ├── nodo.py           # Lógica y estado de cada nodo
    │   ├── enlace.py         # Capa de enlace: delay, bandwidth, transmisión
    │   └── protocolo.py      # Protocolo TCP simplificado (handshake y envío)
    │
    ├── config/
    │   └── escenarios.json   # Definición de escenarios dinámicos
    │
    ├── metricas/
    │   └── calculadora.py    # Métricas: tiempo de envío, eficiencia, latencia
    │
    ├── simulador/
    │   └── main.py           # Secuencia principal de simulación
    │
    └── requirements.txt

## :computer: Componentes Principales

    **Nodo (core/nodo.py)**

    - Encapsula el estado y comportamiento de un dispositivo de red.
    - Gestiona paquetes entrantes/salientes, enlaces, y lógica de protocolo.

    **Enlace (core/enlace.py)**

    - Modela el medio físico (capacidad y latencia).
    - Calcula tiempos de transmisión (tx) y propagación (prop).

    **Protocolo TCP (core/protocolo.py)**

    - Implementación simplificada del TCP:
      SYN, SYN-ACK, ACK para el handshake.
      Transmisión de ráfaga de datos.

    **Calculadora de métricas (metricas/calculadora.py)**

    - Cálculos técnicos:
      Tiempos estimados (Tx, Prop, Total)
      Eficiencia
      Bitrate útil

    **Escenarios (config/escenarios.json)**

    - Configura el entorno sin modificar el código fuente.
    - Incluye: ancho de banda, latencia, tamaño del mensaje, etc.

## :wrench: Instalación y Ejecución

    1. Clonar el repositorio

    `git clone https://github.com/jofsanchezci/Proyecto_Simulador_Network_.git`

    `cd Proyecto_Simulador_Network_`

    `git checkout dev`

    2. Instalar dependencias

    `pip install networkx matplotlib`

    3. Ejecutar simulación

    `python main.py`

## :pencil: Manual de uso

  1. Después de ejecutado el simulador nos solicitará por medio del siguiente mensaje "Ingrese el tiempo de ejecución de la simulación en segundos: " 
     el tiempo por el cual se desea realizar la simulación. 

  2. Al iniciar la ejecución de la simulación en consola desplegará los paquetes enviados.

  3. El número de paquetes es establecido dela siguiente manera:
        La función `random.uniform(1.5, 3)` genera un número decimal aleatorio entre 1.5 y 3. `tiempo_ejecucion * random.uniform(1.5, 3)`
        multiplica el valor de `tiempo_ejecucion` (que debe ser un número) por ese número aleatorio generado. Esto da un número más grande que `tiempo_ejecucion`, de entre 1.5 y 3 veces su valor. `int(...)` convierte el resultado anterior en un entero (descarta los decimales). Lo cual hace que se envie un número de paquetes aleatorio y superior al número
        de segundos de la ejecución.
        
  4. El tamaño son generados aleatoriamente por la función `random.randint(a, b)` en Python, que genera un número entero aleatorio entre a y b, incluyendo ambos extremos. 
     En este caso  es  entre `512 * 1024, 2 * 1024 * 1024`.
  
  5.  **[Simulación] Enviando paquete*
        Se están enviando los paquete.
        
      **[N_Emisor] Enviando datos:* 
        El nodo emisor está enviando un paquete de n tamaño, dado en bits. Este es el tamaño total del paquete que va a ser transmitido.

      **[Enlace] Transmitiendo*
        El enlace de comunicación está llevando a cabo la transmisión del paquete desde el nodo emisor hacia el nodo receptor.
        
      **[Enlace] Tiempo de transmisión:*
        El tiempo de transmisión es el tiempo que tarda en "salir" completamente el paquete del nodo emisor, y depende de la velocidad del enlace.
        
      **[Enlace] Tiempo de propagación:*
        El tiempo de propagación es el tiempo que tarda en viajar una señal desde el emisor al receptor a través del medio físico (fibra, cobre, etc.). lo cual puede depender de la distancia física entre nodos.
        
      **[N_Receptor] Datos recibidos:*
        El nodo receptor, ha recibido el paquete. Nos indicará el tamaño del paquete, es probable que esta cantidad coincida con la parte enviada anteriormente por N_Emisor, lo que confirma que una parte del paquete llegó correctamente.
