# Librerías Utilizadas
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Función para generar una señal de audio (onda sinusoidal)
def generarSeñalAudio(duracion, radioMuestreo, frecuencia, amplitud):
    t = np.linspace(0, duracion, int(radioMuestreo * duracion), endpoint=False)
    señalAudio = amplitud * np.sin(2 * np.pi * frecuencia * t)
    return señalAudio

# Función para trazar el espectrograma de una señal de audio
def trazarEspectrograma(señalAudio, radioMuestreo):
    f, t, Sxx = signal.spectrogram(señalAudio, fs=radioMuestreo)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx))
    plt.title('Espectrograma de la Señal de Audio')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Frecuencia (Hz)')
    plt.colorbar(label='dB')
    plt.show()

# Parámetros de la señal de audio
duracion = 5         # Duración en segundos
radioMuestreo = 44100 # Tasa de muestreo en Hz
frecuencia = 15000      # Frecuencia de la onda sinusoidal en Hz
amplitud = 10000.0      # Aumenta la amplitud (cambia este valor según sea necesario)

# Genera la señal de audio con la amplitud aumentada
señalAudio = generarSeñalAudio(duracion, radioMuestreo, frecuencia, amplitud)

# Trazar el espectrograma de la señal de audio
trazarEspectrograma(señalAudio, radioMuestreo)

