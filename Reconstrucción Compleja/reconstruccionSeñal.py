import numpy as np
import matplotlib.pyplot as plt

# Función para generara una señal de audio senoidal
def generarSeñalAudio(duracion, radioMuestreo, frecuencia):
    vectorTiempo = np.linspace(0, duracion, int(radioMuestreo * duracion), endpoint=False)
    señalAudio = 0.5 * np.sin(2 * np.pi * frecuencia * vectorTiempo)
    return señalAudio

# Función para agregar ruido gaussiano a una señal
def agregarRuido(signal, nivelRuido):
    ruido = np.random.normal(0, nivelRuido, len(signal))
    señalRuido = signal + ruido
    return señalRuido

# Función para eliminar ruido de una señal mediante integración compleja
def recuperarSeñal(señalRuido):
    tamañoFiltro = 5  # Tamaño de la ventana del filtro
    señalFiltrada = np.convolve(señalRuido, np.ones(tamañoFiltro)/tamañoFiltro, mode='same')
    return señalFiltrada

# Graficar las señales original, ruidosa y recuperada
def graficarSeñales(señalOriginal, señalRuido, señalRecuperada, vectorTiempo):
    plt.figure(figsize=(12, 6))
    # Graficar Señal Original
    plt.subplot(3, 1, 1)
    plt.title('Señal Original')
    plt.plot(señalOriginal)
    # Graficar Señal con Ruido
    plt.subplot(3, 1, 2)
    plt.title('Señal Ruidosa')
    plt.plot(señalRuido)
    # Graficar Señal Recuperada
    plt.subplot(3, 1, 3)
    plt.title('Señal Recuperada')
    plt.plot(señalRecuperada)
    # Mostrar las gráficas
    plt.tight_layout()
    plt.show()

# Parámetros de la señal
duracion = 1  # Duración de la señal en segundos
radioMuestreo = 44100  # Tasa de muestreo en Hz
frecuencia = 5.0  # Frecuencia en Hz (A4)

# Generar la señal de audio original
señalOriginal = generarSeñalAudio(duracion, radioMuestreo, frecuencia)

# Configurar el nivel de ruido gaussiano que deseas agregar
nivelRuido = 0.1

# Agregar ruido gaussiano a la señal original
señalRuido = agregarRuido(señalOriginal, nivelRuido)

# Recuperar la señal original
señalRecuperada = recuperarSeñal(señalRuido)



