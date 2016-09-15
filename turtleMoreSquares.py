__author__ = 'student'
import turtle
for i in range (50,550,50):
    turtle.shape('turtle')
    turtle.pendown()
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.forward(i)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-i/2,-i/2)
