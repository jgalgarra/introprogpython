# Archivo: bucles.py
# Autor: Javier Garcia Algarra 
# Fecha: 27 de diciembre de 2017
# Descripción: Variables booleanas


# El bucle while se ejecuta mientras la condición sea verdad

variable_a = 1

while (variable_a < 7):
    print("El valor de variable_a es",variable_a,"y como es menor que 7 entramos en el bucle")
    variable_a = variable_a + 1
    
print("Cuando la variable_a vale",variable_a,"salimos del bucle")

# Espera
dummy = input()

print("Bucle for")
# La instrucción for repite el código para todos los elementos de la lista
for i in [9,8,5]:
    print("El valor de i es",i)
    
# Espera
dummy = input()

# Una forma muy habitual de usar el bucle for es con una secuencia de números
# La función range() devuelve una lista entre dos números o entre 0 y n-1 si solo
# indicamos un número. Veamos su utilidad

print()                                     # Linea en blanco
print("Queremos repetir un bucle 7 veces")
veces = 0
for i in range(7):
    veces = veces + 1
    print("Veces que he pasado por el bucle",veces,"y el valor de i es",i)

# Espera
dummy = input()
    
print()                                     # Linea en blanco
print("Vamos a calcular la suma de los números 1 al 10")
suma = 0
for i in range(1,11):    # Cuando pones dos números range genera desde el mínimo hasta el máximo menos 1
    suma = suma + i
    print("El valor de i es",i)
print("La suma de los 10 primeros números enteros vale",suma)