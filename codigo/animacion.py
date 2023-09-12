# Archivo: animaciones.py
# Basado en https://matplotlib.org/examples/animation/simple_anim.html
# Autor: Javier Garcia Algarra 
# Fecha: 28 de diciembre de 2017
# Descripción: Ejemplo de animacion

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

PI = 3.1416
fig, ax = plt.subplots()

x = np.arange(0, 4*PI, 0.01)
line, = ax.plot(x, np.sin(x))


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,


def animate_sin_wave(i):
    line.set_ydata(np.sin(x+ i/10.0))  # update the data
    return line,

def animate_square_wave(i):
    line.set_ydata(0.5*((4/PI)*np.sin(x+ i/10.0)+(4/(3*PI))*np.sin(3*(x+ i/10.0))+(4/(5*PI))*np.sin(5*(x+ i/10.0)))) # update the data
    return line,

def animate_noisy_wave(i):
    line.set_ydata(0.5*(np.sin(x+ i/10.0)+0.4*np.random.random(size=len(x)))) # update the data
    return line,

speed = 20
frames = 200

# Quitar el comentario de ls función de onda que se representa: seno, seno con ruido gaussiano o 'cuadrada'
#funcion = animate_sin_wave
#funcion = animate_noisy_wave
funcion = animate_square_wave

ani = animation.FuncAnimation(fig, funcion, np.arange(1, frames), init_func=init,
                          interval=speed, blit=True)
plt.show()

