__author__ = 'student'
__author__ = 'student'
import turtle
import math

R=50
n=100
def circ(r):
    turtle.left(360/n)
    turtle.forward(2*R*math.sin(math.pi/n))
for i in range (30):
    #turtle.circle(R+5*i)
    #turtle.circle(-R-5*i)
    circ(R+5*i)
for i in range (300):
    circ(-R-5*i)
