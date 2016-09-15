import turtle as tr

tr.shape('turtle')
for i in range(0,10):
    tr.forward(50 + i*2*50**0.5)
    tr.left(90)
    tr.forward(50 + i*2*50**0.5)
    tr.left(90)
    tr.forward(50 + i*2*50**0.5)
    tr.left(90)
    tr.forward(50 + i*2*50**0.5)
    tr.penup()
    tr.right(45)
    tr.forward(10)
    tr.left(135)
    tr.pendown()