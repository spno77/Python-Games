#Pong in Python3

import turtle

wn = turtle.Screen()
wn.title(" Pong ")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #the speed of animation(maximum speed)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #the speed of animation(maximum speed)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)


#Main game loop
while True:
	wn.update()




