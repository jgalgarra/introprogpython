# Archivo: tortuga_1_movimiento.py
# Autor: Javier Garcia Algarra 
# Fecha: 27 de diciembre de 2017
# Descripción: Ejemplo de uso de la tortuga gráfica

import turtle
import random
    
print("Vamos a dibujar un cuadrado")
# Dibujamos un rectángulo de lado 200
lado = 200
for i in range(4):
    turtle.forward(lado)
    turtle.left(90)

print("Impresionante, ¿no?")
print("Ahora voy a dibujar otro de color rojo")
dummy = input("Pulsa cualquier tecla para que comience")

turtle.penup()               # Levanta la pluma del papel
turtle.setpos(-lado,-lado)   # Muevete a esta posicion
turtle.pendown()             # Vuelve a poner la pluma en el papel
turtle.color("red")
for i in range(4):
    turtle.forward(lado)
    turtle.left(90)

print("Ahora vamos a hacer que el ratón se mueva al azar (random walk)")
dummy = input("Pulsa cualquier tecla para que comience ")
turtle.clear()
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
saltos = 0
while (saltos < 20):
    turtle.forward(25)
    angulo_al_azar = random.randrange(0,360)
    turtle.left(angulo_al_azar)
    saltos = saltos + 1

print("Una estrella...")
dummy = input("Pulsa cualquier tecla para que comience ")
turtle.clear()
turtle.penup()
turtle.setpos(-100,-100)
turtle.pendown()
puntas = 0
while (puntas < 8):
    turtle.forward(200)
    turtle.left(135)
    puntas = puntas + 1

print("Para el final dejamos lo mejor...")
dummy = input("Pulsa cualquier tecla para que comience ")
turtle.penup()
turtle.setpos(100,100)
turtle.pendown()
turtle.color('red', 'yellow')
turtle.begin_fill()
puntas = 0
while (puntas < 36):
    turtle.forward(200)
    turtle.left(170)
    puntas = puntas + 1

turtle.end_fill()
turtle.done()