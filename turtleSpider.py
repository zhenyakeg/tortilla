__author__ = 'student'
import turtle
import time
n=int(input())
for i in range (0,n):
    turtle.shape('turtle')
    turtle.forward(150)
    turtle.left(180)
    turtle.forward(150)
    turtle.right(180+360/n)


time.sleep(10)