import numpy as np
import matplotlib.pyplot as plt

# Función para modificar la fase de una señal de audio.
def modificarFase(señalAudio, gradosDesfase):
   
    # Convierte el cambio de fase de grados a radianes
    radianesDesfase = np.radians(gradosDesfase)

    # Aplica el cambio de fase
    señalModificada = np.abs(señalAudio) * np.exp(1j * (np.angle(señalAudio) + radianesDesfase))
    
    return señalModificada

def graficarSeñales(señalOriginal, señalModificada, vectorTiempo):
    # Graficar la señal original y la señal con la fase modificada
    plt.figure(figsize=(12, 4))
    plt.subplot(2, 1, 1)
    plt.plot(vectorTiempo, señalOriginal)
    plt.title('Señal Original')
    plt.subplot(2, 1, 2)
    plt.plot(vectorTiempo, np.real(señalModificada))
    plt.title('Señal con Fase Modificada')
    plt.tight_layout()
    plt.show()

# Crear una señal de audio (por ejemplo, una onda sinusoidal)
duracion = 2
radioMuestreo = 44100
frecuencia = 10
vectorTiempo = np.linspace(0, duracion, int(radioMuestreo * duracion), endpoint=False)
señalAudio = np.sin(2 * np.pi * frecuencia * vectorTiempo) * 10

# Modificar la fase de la señal en 45 grados (pi/4 radianes)
gradosDesfase = 180
señalModificada = modificarFase(señalAudio, gradosDesfase)

# Mostrar ambas señales
graficarSeñales(señalAudio, señalModificada, vectorTiempo)
