#Pong in Python3

import turtle

wn = turtle.Screen()
wn.title(" Pong ")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


#Main game loop
while True:
	wn.update()
