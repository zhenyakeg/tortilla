import turtle as tr
import numpy as np

def rf(r,f):
    return(r*np.cos(f),r*np.sin(f))

tr.shape('turtle')

for i in range(0,36):
    tr.forward(10)
    tr.left(10)
for i in range(0,36):
    tr.forward(10)
    tr.right(10)
tr.right(45)
for i in range(0,36):
    tr.forward(10)
    tr.left(10)
for i in range(0,36):
    tr.forward(10)
    tr.right(10)
tr.right(45)
for i in range(0,36):
    tr.forward(10)
    tr.left(10)
for i in range(0,36):
    tr.forward(10)
    tr.right(10)