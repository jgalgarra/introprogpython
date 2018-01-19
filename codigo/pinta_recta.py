# Archivo: pinta_recta.py
# Autor: Javier Garcia Algarra 
# Fecha: 24 de diciembre de 2017
# Descripción: Dibujamos una linea recta

import matplotlib.pyplot as plt

# Funcion para crear una lista de numeros que empieza en inferior y termina en superior
def crea_lista_de_valores(inferior, superior):
    listadevalores = []                          # Creamos una lista vacia
    for j in range(inferior,superior+1):         # La variable j va tomando los valores del rango inferior a superior
        listadevalores.append(j)                 # Cada valor de la variable j se añade a la lista
    return(listadevalores)                       # Se devuelve la lista completa

# Crear una lista de números enteros, del 1 al 10
x_valores = crea_lista_de_valores(1,10)

# Ahora vamos a crear los valores y. La formula de la recta es y = 2 * x
# Recorremos los valores de x para crear otra lista de valores y
# La lista de valores x es [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y la lista de valores y será [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

y_valores = []
for k in x_valores:
    y_valores.append(2 * k)
    
# Parte del programa que pinta la gráfica. Pasamos a la funcion plt.plot las listas de valores x e y
plt.plot(x_valores, y_valores, ".")
plt.ylabel('y')            # Etiqueta del eje y. Podriamos no ponerla
plt.xlabel('x')            # Etiqueta del eje x
plt.show()                 # Esta función ordena mostrar la imagen en una ventanita nueva
