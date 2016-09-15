__author__ = 'student'
import turtle
import math
def angles(R, n):
    a=math.sin(2*math.pi/2/n)*2*R
    turtle.pendown()
    alp=180*(n-2)/n
    turtle.left(180-alp/2)
    for i in range (n):
        turtle.forward(a)
        turtle.left(180-alp)
    turtle.right(180-alp/2)

n=3
R=30
for i in range (1,11,1):
    turtle.penup()
    turtle.goto(R, 0)
    angles(R, n)
    n+=1
    R += 20