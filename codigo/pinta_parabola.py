# Archivo: pinta_parabola.py
# Autor: Javier Garcia Algarra 
# Fecha: 24 de diciembre de 2017
# Descripción: Dibujamos una parábola

import matplotlib.pyplot as plt

# Funcion para crear una lista de numeros que empieza en inferior y termina en superior
def crea_lista_de_valores(inferior, superior):
    listadevalores = []                          # Creamos una lista vacia
    for j in range(inferior,superior+1):         # La variable j va tomando los valores del rango inferior a superior
        listadevalores.append(j)                 # Cada valor de la variable j se añade a la lista
    return(listadevalores)                       # Se devuelve la lista completa

# Crear una lista de números naturales, del -15 al 15
x_valores = crea_lista_de_valores(-15,15)

# Ahora vamos a crear los valores y. La formula de la parábola es y =  x ^ 2
# Recorremos los valores de x para crear otra lista de valores y
# La lista de valores x es [-15, ..., -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, ..., 15]


y_valores = []
for k in x_valores:
    y_valores.append(k ** 2)
    
# Parte del programa que pinta la gráfica. Pasamos a la funcion plt.plot las listas de valores x e y
plt.plot(x_valores, y_valores)
plt.ylabel('y')            # Etiqueta del eje y. Podriamos no ponerla
plt.xlabel('x')            # Etiqueta del eje x
plt.show()                 # Esta función ordena mostrar la imagen en una ventanita nueva