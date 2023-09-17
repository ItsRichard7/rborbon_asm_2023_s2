import numpy as np

# Función para modificar la fase de una señal de audio.
def modificarFase(señalAudio, gradosDesfase):
   
    # Convierte el cambio de fase de grados a radianes
    radianesDesfase = np.radians(gradosDesfase)
    
    # Aplica el cambio de fase
    señalModificada = np.abs(señalAudio) * np.exp(1j * (np.angle(señalAudio) + radianesDesfase))
    
    return señalModificada
