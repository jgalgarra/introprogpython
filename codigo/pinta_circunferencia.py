# Archivo: pinta_parabola.py
# Autor: Javier Garcia Algarra 
# Fecha: 24 de diciembre de 2017
# Descripción: Dibujamos una circunferencia

import matplotlib.pyplot as plt
import math                                      # importamos la librería matemática que sabe hacer raíces cuadradas

# Funcion para crear una lista de numeros que empieza en inferior y termina en superior
def crea_lista_de_valores(inferior, superior):
    listadevalores = []                          # Creamos una lista vacia
    for j in range(inferior,superior+1):         # La variable j va tomando los valores del rango inferior a superior
        listadevalores.append(j)                 # Cada valor de la variable j se añade a la lista
    return(listadevalores)                       # Se devuelve la lista completa

# Crear una lista de números naturales, del -9 al 9
x_valores = crea_lista_de_valores(-9,9)

# Ahora vamos a crear los valores y. La formula de la circunferencia es y**2 + x**2 = radio**2
# Recorremos los valores de x para crear otra lista de valores y
# pero para cada valor de x hay dos valores de y, el positivo y el negativo de la raiz cuadrada.
# Para solucionarlo creamos dos listas de valores y, una positiva y otra negativa

radio = 9
y_valores_pos = []
y_valores_neg = []

for k in x_valores:
    y_valores_pos.append(math.sqrt(radio**2 - k**2))
    y_valores_neg.append(-math.sqrt(radio**2 - k**2))
  
# Parte del programa que pinta la gráfica. Pasamos a la funcion plt.plot las listas de valores x e y
plt.plot(x_valores, y_valores_pos, ".")
plt.plot(x_valores, y_valores_neg, ".")    # Añadimos la lista de valores y negativos al gráfico
plt.axis('equal')
plt.ylabel('y')            # Etiqueta del eje y. Podriamos no ponerla
plt.xlabel('x')            # Etiqueta del eje x
plt.show()                 # Esta función ordena mostrar la imagen en una ventanita nueva
