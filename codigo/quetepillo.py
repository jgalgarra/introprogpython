# Archivo: quetepillo.py
# Autor: Javier Garcia Algarra 
# Fecha: 27 de diciembre de 2017
# Descripción: Juego de la presa y el cazador
#
# La tortuga naranja se mueve al azar. El cazador es la tortuga negra.
# Podemos controlar su dirección haciendo que gire con las flechas izquierda
# y derecha. Si pulsamos la flecha hacia arriba el cazador acelera el paso
# El juego termina cuando el cazador alcanza a la presa

from turtle import *
import random
import math

# Creacion de la pantalla
dimension = 500
setup(dimension, dimension)
salto = int(dimension/50)
wn = Screen()
se_acabo = False
title("Que te pillo")

# La presa de color naranja se coloca en el centro
presa = Turtle()
presa.penup()
presa.setpos(0,0)
presa.color("orange")
presa.showturtle()

# El cazador empieza en una posición aleatoria
mitortuga = Turtle()
mitortuga.penup()
mitortuga.setpos(random.randrange(-int(dimension/3)-50,int(dimension/3)+50),random.randrange(-int(dimension/3),int(dimension/3)))
mitortuga.showturtle()

# Cálculo de la distancia entre la presa y el cazador
def calc_distancia(posA,posB):
    distancia =math.sqrt( (posA[0]-posB[0])**2+(posA[1]-posB[1])**2 )
    return(distancia)

# Funciones para controlar el movimiento del cazador
def k1():                             # Flecha superior
    if not(se_acabo):
        mitortuga.penup()
        mitortuga.forward(salto) 
def k2():                             # Flecha izquierda
    mitortuga.left(45)

def k3():
    mitortuga.right(45)               # Flecha derecha
    
def movepresa():                      # Movimiento de la presa
# Esta función se ejecuta cada vez que vence el temporizador de 0.1 segundos
    global contador, se_acabo
    if not(se_acabo):
        contador = contador + 1
        mitortuga.penup()
        mitortuga.forward(salto/4)    # Movimiento lento del cazador
        dist = calc_distancia(mitortuga.pos(),presa.pos()) # Calcular la distancia
        if dist <= 6:                 # Condición de caza
            print("¡¡¡Te pillé!!!. Has necesitado",contador/10,"segundos.")
            se_acabo = True
            done()
        if not(contador % 10):        # Imprimir el tiempo cada segunfo
            print("Segundos: ",contador / 10)
        random_walk = random.randrange(4)  # Movimiento aleatorio de la presa
        if random_walk < 2:                # Si es 0 ó 1 saltar
            presa.forward(salto)
        if random_walk == 2:               # Girar a la izquierda
            presa.left(random.randrange(90))
        if random_walk == 3:               # Girar a la derecha
            presa.right(random.randrange(90))
        wn.ontimer(movepresa, periodo)     # Reiniciar el contador

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
periodo = 100
contador = 0
wn.ontimer(movepresa, periodo)
listen()

mainloop()
