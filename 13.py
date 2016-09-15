import turtle as tr

tr.shape('turtle')
tr.color("black","yellow")
tr.begin_fill()
for i in range(0,72):
    tr.forward(10)
    tr.left(5)
tr.end_fill()
tr.penup()
tr.color("black","red")
tr.goto(-40,170)
tr.begin_fill()
for i in range(0,72):
    tr.forward(1)
    tr.left(5)
tr.end_fill()
tr.goto(40,170)
tr.begin_fill()
for i in range(0,72):
    tr.forward(1)
    tr.left(5)
tr.end_fill()
tr.right(90)
tr.goto(0,150)
tr.width(5)
tr.color("black","black")
tr.pendown()
tr.forward(50)
tr.penup()
tr.goto(-60,90)
tr.pendown()
def duga(r,n,dr):
    tr.shape('turtle')
    for i in range(1,51,1):
        tr.forward(r)
        tr.left(180-180*(n-2)/n)
    return()
duga(4,100,1)