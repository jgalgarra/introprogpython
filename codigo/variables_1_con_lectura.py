# Archivo: variables_1_con_lectura.py
# Autor: Javier Garcia Algarra 
# Fecha: 27 de diciembre de 2017
# Descripción: Lectura de variables desde el teclado

# Primero preguntamos al usuario cual es su nombre
print("Dime tu nombre, por favor: ")
nombre = input()                         # Esta función lee la variable nombre desde el teclado
# Repetimos la operación para saber la edad, el peso y la altura
print("¿Cuál es tu edad?: ")
edad = input()  
print("¿Cuántos kilos pesas?: ")
peso = input()
print("¿Cuántos centímetros mides?: ")
estatura = input()

# Este programa tan simple lo único que hace es construir un mensaje con la información que
# nos dió el usuario
print("Hola",nombre,". Tu edad son",edad,"años, pesas",peso,"kilos y mides",estatura," cm")

# Hay otra manera más compacta de escribir el mensaje y leer la variable de entrada
tu_ciudad = input("¿En qué ciudad vives?: ")
print(tu_ciudad,"es un lugar muy agradable para vivir,",nombre)

# También podemos indicar a Python de qué tipo es la variable que se desea leer. Por ejemplo
# queremos que la edad sea un número y no una cadena de caracteres
edad = int(input("¿Puedes repetirme la edad, por favor?: "))
print("Nadie diría que tienes",edad,"años. Pareces más joven :)")

