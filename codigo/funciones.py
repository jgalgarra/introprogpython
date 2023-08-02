# Archivo: funciones.py
# Autor: Javier Garcia Algarra 
# Fecha: 27 de diciembre de 2017
# Descripción: Manejo simple de funciones


# En programación no es buena práctica repetir código
# Volvamos al ejemplo del bucle for. Queremos calcular la suma de los 10 primeros enteros

print("Vamos a calcular la suma de los números 1 al 10")
suma = 0
for i in range(1,11):    # Cuando pones dos números range genera desde el mínimo hasta el máximo menos 1
    suma = suma + i
print("La suma de los 10 primeros números enteros vale",suma)

# Espera
dummy = input()

# Imagina que ahora quieres calcular la suma de los 8 primeros enteros. Podemos repetir el código
# y cambiar el límite

print("Vamos a calcular la suma de los números 1 al 8")
suma = 0
for i in range(1,9):    # Cuando pones dos números range genera desde el mínimo hasta el máximo menos 1
    suma = suma + i
print("La suma de los 8 primeros números enteros vale",suma)

# Esto queda muy feo, hay una manera de hacerlo mejor, con funciones

def suma_primeros_enteros(hasta_que_numero):       # hasta_que_numero es un parámetro de entrada
    suma = 0
    for i in range(1,hasta_que_numero+1):    # Cuando pones dos números, range genera una lista de números desde el mínimo hasta el máximo menos 1
        suma = suma + i
    return(suma)            # Valor que devuelve la función

print()
print("La suma de los primeros 5 números enteros vale",suma_primeros_enteros(5))
print("La suma de los primeros 12 números enteros vale",suma_primeros_enteros(12))

# Espera
dummy = input()

# Vamos a jugar poniendo junto todo lo que ya sabemos.
# ¿Qué crees que sucederá con este trozo de código?

valor_suma = 0
while (valor_suma < 500):
    num_enteros = int(input("¿Cuántos de los primeros enteros quieres que sume? "))
    valor_suma = suma_primeros_enteros(num_enteros)
    print("El valor de la suma de los",num_enteros,"primeros enteros es",valor_suma)
    print()
