from turtle import *
import random
import math

dimension = 500
setup(dimension, dimension)
salto = int(dimension/50)
wn = Screen()
se_acabo = False
title("Que te pillo")
mitortuga = Turtle()

mitortuga.penup()

mitortuga.setpos(random.randrange(-int(dimension/3),int(dimension/3)),random.randrange(-int(dimension/3),int(dimension/3)))
mitortuga.showturtle()


presa = Turtle()
presa.penup()
presa.setpos(0,0)
presa.color("orange")
presa.forward(salto)
presa.showturtle()

def calc_distancia(posA,posB):
    distancia =math.sqrt( (posA[0]-posB[0])**2+(posA[1]-posB[1])**2 )
    return(distancia)

def k1():
    if not(se_acabo):
        mitortuga.penup()
        mitortuga.forward(salto) 
def k2():
    mitortuga.left(45)

def k3():
    mitortuga.right(45)
    
def movepresa():
    global contador, se_acabo
    if not(se_acabo):
        contador = contador + 1
        mitortuga.penup()
        mitortuga.forward(salto/4)
        dist = calc_distancia(mitortuga.pos(),presa.pos())
        if dist <= 6:
            print("¡¡¡Te pillé!!!. Has necesitado",contador/10,"segundos.")
            se_acabo = True
            done()
        if not(contador % 10):
            print("Segundos: ",contador / 10)
        random_walk = random.randrange(4)
        if random_walk < 2:
            presa.forward(salto)
        if random_walk == 2:
            presa.left(random.randrange(90))
        if random_walk == 3:
            presa.right(random.randrange(90))
        wn.ontimer(movepresa, periodo)
##def k4():
##    mitortuga.back(45)

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
#onkey(k4, "Down")
periodo = 100
contador = 0
wn.ontimer(movepresa, periodo)
listen()

mainloop()