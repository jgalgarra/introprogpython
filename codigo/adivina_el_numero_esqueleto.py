# Archivo: adivina_el_numero.py
# Autor: Javier Garcia Algarra 
# Fecha: 27 de diciembre de 2017
# Descripción: Juego para adivinar un número secreto

import random                 # Este paquete es necesario para generar números aleatorios

print("Hola, vamos a jugar a adivinar un número secreto entre 1 y 100")

# Elegir al azar un número entero entre 1 y 100
numero_secreto = random.randrange(...)

print("Ya lo he pensado, podemos empezar")
intentos = 1                  # Contador de intentos. Empieza en uno

# Esta funcion pide al usuario un número. Si es igual devolverá el valor True, el usuario
# acertó. Si no, dará una pista indicando si el número secreto es mayor o menor que el que
# escribió el jugador.
def adivinalo(numintentos, numsec):
    # Leer el numero del jugador

    # Si el numero leido es el mismo decir que ha adivinado en n intentos
    # y devolver la variable acierto a True
    if (numero_humano == numsec):
        acierto = True

    # En caso contrario 
    else:
        # La variable acierto es False
        acierto = False
        # Si el numero es menor decírselo al jugador

        # Si no indicar que es mayor

        # Indicar el 
    return(acierto)

# Bucle principal del programa. Mientras el usuario no adivine el número repetimos
# la jugada e incrementamos el número de intentos
while not(adivinalo(intentos, numero_secreto)): 
    intentos = intentos + 1
                        
    
