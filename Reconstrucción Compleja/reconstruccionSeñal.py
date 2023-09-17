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



