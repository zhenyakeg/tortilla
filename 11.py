import turtle as tr

def crc(r,k,dr):
    tr.shape('turtle')
    for p in range(0,k):
        for i in range(0,36):
            tr.forward(r)
            tr.left(10)
        for i in range(0,36):
            tr.forward(r)
            tr.right(10)
        r = r + dr

eval(crc(10,3,2))