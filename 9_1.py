import turtle as tr
import numpy as np

def rf(r,f):
    return(r*np.cos(f),r*np.sin(f))

def multi(n,k,r,dr):
    tr.shape('turtle')
    for s in range(0,k):
        tr.penup()
        tr.goto(r,0)
        tr.pendown()
        for i in range(0,n):
            tr.goto(rf(r,(np.pi*2/n)*(i+1)))
        r=r+dr
        n=n+1

eval(multi(9,5,100,50))