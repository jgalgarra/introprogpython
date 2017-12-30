# Archivo: variables_2_listas.py
# Autor: Javier Garcia Algarra 
# Fecha: 27 de diciembre de 2017
# Descripción: Manejo de listas


# En una lista podemos incluir diferentes valores

lista_a = ["hola","mundo","hasta","luego"]

# Si imprimimos la lista por la pantalla aparecerán los elementos individuales
print(lista_a)

# La longitud de una lista y de cualquier variable se puede saber con la función len
print("La lista tiene",len(lista_a),"elementos")

# Los elementos de una lista pueden conocerse de manera individual. Python cuenta
# desde 0 hasta longitud de la lista - 1
print("El primer elemento de la lista es",lista_a[0])
print("El último elemento es",lista_a[len(lista_a)-1])

# Podemos agregar elementos al final de una lista con el método append. Es muy
# sencillo
otro_elemento = input("Escribe el valor de un nuevo elemento para la lista: ")
lista_a.append(otro_elemento)
print("Ahora la longitud de la lista es",len(lista_a))
print("Puedes comprobarlo tú mismo")
print(lista_a)

# Si queremos que el programa se detenga hasta que el usuario pulse cualquier tecla
# podemos usar una variable 'tonta' que no haga nada, solo esperar

dummy = input()

print("Ahora vamos a ver como funcionan las listas de números")
# También podemos tener listas de números
lista_b = [8, 9, 10, 4]
# Python es muy inteligente y puede sumar todos los elementos de una vez
suma_lista_b = sum(lista_b)
print("Los valores de la lista numérica son ",lista_b,"y su suma es",suma_lista_b)
# También sabe hallar el máximo y el mínimo
maximo = max(lista_b)
minimo = min(lista_b)
print("El valor máximo es",maximo,"y el mínimo es",minimo)
