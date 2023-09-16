# Librerías Utilizadas
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Función para generar una señal de audio (onda sinusoidal)
def generarSeñalAudio(duracion, radioMuestreo, frecuencia, amplitud):
    t = np.linspace(0, duracion, int(radioMuestreo * duracion), endpoint=False)
    señalAudio = amplitud * np.sin(2 * np.pi * frecuencia * t)
    return señalAudio



