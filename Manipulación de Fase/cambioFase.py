import numpy as np
import matplotlib.pyplot as plt

# Función para modificar la fase de una señal de audio.
def modificarFase(señalAudio, gradosDesfase):
    transformada = np.fft.fft(señalAudio)
    magnitudTr = np.abs(transformada)
    faseTr = np.angle(transformada)
    radianesDesfase = np.deg2rad(gradosDesfase) # Convierte el cambio de fase de grados a radianes
    faseMod = faseTr + radianesDesfase # Nueva fase de la señal
    tranformadaMod = magnitudTr * np.exp(1j * faseMod) # Aplica el cambio de fase

    señalModificada = np.fft.ifft(tranformadaMod)

    return señalModificada

# Graficar la señal original y la señal con la fase modificada
def graficarSeñales(señalOriginal, señalModificada, vectorTiempo):
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
duracion = 1
radioMuestreo = 44100
frecuencia = 5
vectorTiempo = np.linspace(0, duracion, int(radioMuestreo * duracion), endpoint=False)
señalAudio = np.sin(2 * np.pi * frecuencia * vectorTiempo)

# Solicitar al usuario el desfase que desea aplicar
gradosDesfaseInput = input('>>> Inserte los grados de desfase que desea aplicar <<< \n')
gradosDesfase = float(gradosDesfaseInput)
señalModificada = modificarFase(señalAudio, gradosDesfase)

# Mostrar ambas señales
graficarSeñales(señalAudio, señalModificada, vectorTiempo)
