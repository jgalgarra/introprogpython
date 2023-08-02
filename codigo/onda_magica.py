# Archivo: onda_magica.py
# Autor: Javier Garcia Algarra 
# Fecha: 28 de diciembre de 2017
# Descripción: Ejemplo de suma de series de Fourier

import matplotlib.pyplot as plt
import math                                      # importamos la librería matemática que sabe calcular el seno

PI = 3.1416                                      # definimos la constante PI

# Funcion para crear una lista de numeros que empieza en inferior y termina en superior con un paso no entero
def crealistadevaloresreales(inferior, superior, paso):
    listadevalores = []                          # Creamos una lista vacia
    j = inferior
    while (j < superior):                        
        listadevalores.append(j)                 # Cada valor de la variable j se añade a la lista
        j = j + paso
    return(listadevalores)                       # Se devuelve la lista completa

# Crear una lista de números entre 0 y 4*PI
x_valores = crealistadevaloresreales(0,4*PI,0.1)

# Ahora vamos a crear los valores y. 

y_sin = []

for k in x_valores:
    y_sin.append((4/PI)*math.sin(k))

# Parte del programa que pinta la gráfica. Pasamos a la funcion plt.plot las listas de valores x e y
plt.plot(x_valores, y_sin)
plt.axis('equal')
plt.ylabel('y')            # Etiqueta del eje y. Podriamos no ponerla
plt.xlabel('x')            # Etiqueta del eje x
plt.show()                 # Esta función ordena mostrar la imagen en una ventanita nueva

dummy = input("Muy hermosa la función sen(x), ahora vamos a ver como es sen(3x)")
y_3sin = []

for k in x_valores:
    y_3sin.append((4/(3*PI))*math.sin(3*k))
plt.plot(x_valores, y_sin, '--')
plt.plot(x_valores, y_3sin, color = 'red')
plt.axis('equal')
plt.ylabel('y')            # Etiqueta del eje y. Podriamos no ponerla
plt.xlabel('x')            # Etiqueta del eje x
plt.show()                 # Esta función ordena mostrar la imagen en una ventanita nueva

print("")
dummy = input("Muy hermosa la función sen(3x), ahora vamos a ver como es sen(5x)")
y_5sin = []

for k in x_valores:
    y_5sin.append((4/(5*PI))*math.sin(5*k))
plt.plot(x_valores, y_sin,'--')
plt.plot(x_valores, y_3sin,'--', color = 'red')
plt.plot(x_valores, y_5sin, color = 'green')
plt.axis('equal')
plt.ylabel('y')            # Etiqueta del eje y. Podriamos no ponerla
plt.xlabel('x')            # Etiqueta del eje x
plt.show()                 # Esta función ordena mostrar la imagen en una ventanita nueva

print("")
dummy = input("¿Qué crees que pasa si sumamos las tres ondas?")

y_suma = []
for i in range(len(x_valores)):
    y_suma.append(y_sin[i] + y_3sin[i] + y_5sin[i], )
plt.plot(x_valores, y_sin,'--')
plt.plot(x_valores, y_3sin,'--', color = 'red')
plt.plot(x_valores, y_5sin,'--', color = 'green')
plt.plot(x_valores, y_suma, color = 'black',lw=3)
plt.axis('equal')
plt.ylabel('y')            # Etiqueta del eje y. Podriamos no ponerla
plt.xlabel('x')            # Etiqueta del eje x
plt.show()                 # Esta función ordena mostrar la imagen en una ventanita nueva
