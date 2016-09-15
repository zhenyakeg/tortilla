__author__ = 'student'
import turtle

r1 = 20
dr = 5
n = 10
N = 20

for i in range (r1,r1+n*dr,dr):
    turtle.left()
    turtle.forward(i)