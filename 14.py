import turtle as tr
import numpy as np

def rf(r,f):
    return(r*np.cos(f),r*np.sin(f))

def multi(r):
    tr.shape('turtle')
    tr.penup()
    tr.goto(rf(r,(np.pi*2/5)*(1)))
    tr.pendown()
    tr.goto(rf(r,(np.pi*2/5)*(3)))
    tr.goto(rf(r,(np.pi*2/5)*(5)))
    tr.goto(rf(r,(np.pi*2/5)*(2)))
    tr.goto(rf(r,(np.pi*2/5)*(4)))
    tr.goto(rf(r,(np.pi*2/5)*(1)))

eval(multi(100))