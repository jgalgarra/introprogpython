# Archivo: variables_3_booleanas.py
# Autor: Javier Garcia Algarra 
# Fecha: 27 de diciembre de 2017
# Descripción: Variables booleanas


# Las variables booleanas son muy útiles. Sólo pueden tomar dos variables True (Verdadero) o False (Falso)

booleana_1 = True
booleana_2 = False

print("La variable booleana_1 es",booleana_1,"y la variable 2 es",booleana_2)

# Espera
dummy = input()

# Cuando hacemos comparaciones el resultado es una variable booleana
a = 6
b = 5
a_mayor_que_b = (a > b)
a_menor_que_b = (a < b)
print("La variable a vale",a,"y la variable b vale",b)
print("Si digo que a es mayor que b, es",a_mayor_que_b)
print("Si digo que a es mayor que b, es",a_menor_que_b)

# Espera
dummy = input()

# Para saber si dos valores son iguales usamos el operador ==
# ¡Cuidado! si pones solo = es el operador de asignación y

d = 5
e = 5
f = 7

print("Las variables d, e y f valen",d,",",e,",",f)
print("Si digo que d y e valen lo mismo es", d == e)
print("Si digo que e y f valen lo mismo es", e == f)

# Espera
dummy = input()

# Con las variables booleanas podemos tomar decisiones usando
# la expresión if
if (5 > 3):
    print("La condición 5 > 3 se cumple")
          
# Espera
dummy = input()

# ¿Qué sucede si queremos hacer una cosa si la condición se cumple y
# otra diferente si no se cumple? Para eso usamos la expresión completa if ... else

y = 7
x = 9

print("Las variables x, y valen",x,",",y)
if (x == y):
    print("Esto es lo sucede si las variables x e y son iguales")
else:
    print("Y esto es lo que sucede si las variables x e y no son iguales")
    
          
# Espera
dummy = input()

# Ahora vamos a ver un ejemplo muy sencillo. Luego lo haremos un poco más divertido con un juego
numero_secreto = 7            # OK, no es muy secreto porque ya sabes programar en Python, pero lo es para alguien que solo use el programa
num_del_usuario = int(input("He pensado un número secreto del 1 al 10. A ver si lo adivinas "))

if (num_del_usuario == numero_secreto):
    print("¡Impresionante!, lo adivinaste")
else:
    print("No acertaste, mi número secreto era el ",numero_secreto)
