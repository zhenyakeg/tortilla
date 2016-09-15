import turtle as tr

def multi(n,p,k):
    tr.shape('turtle')
    for i in range(0,k):
        for i in range(0,n):
            tr.forward(p/n)
            tr.left(180-180*(n-2)/n)
        tr.penup()
        tr.right(90)
        tr.forward(50)
        tr.left(90)
        tr.pendown()
        n = n + 1
        p = p + 500
    return

eval(multi(3,200,12))