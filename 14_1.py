import turtle as tr
import numpy as np

def rf(r,f):
    return(r*np.cos(f),r*np.sin(f))

def multi(r):
    tr.shape('turtle')
    tr.penup()
    tr.goto(rf(r,(np.pi*2/11)*(1)))
    tr.pendown()
    tr.goto(rf(r,(np.pi*2/11)*(6)))
    tr.goto(rf(r,(np.pi*2/11)*(11)))
    tr.goto(rf(r,(np.pi*2/11)*(5)))
    tr.goto(rf(r,(np.pi*2/11)*(10)))
    tr.goto(rf(r,(np.pi*2/11)*(4)))
    tr.goto(rf(r,(np.pi*2/11)*(9)))
    tr.goto(rf(r,(np.pi*2/11)*(3)))
    tr.goto(rf(r,(np.pi*2/11)*(8)))
    tr.goto(rf(r,(np.pi*2/11)*(2)))
    tr.goto(rf(r,(np.pi*2/11)*(7)))
    tr.goto(rf(r,(np.pi*2/11)*(1)))

eval(multi(100))