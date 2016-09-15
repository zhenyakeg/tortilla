import turtle as tr

def duga(r,n,dr):
    tr.shape('turtle')
    for i in range(1,51,1):
        tr.forward(r)
        tr.left(180-180*(n-2)/n)
    for i in range(1,51,1):
        tr.forward(dr)
        tr.left(180-180*(n-2)/n)
    return()
duga(4,100,1)