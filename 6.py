import turtle as tr
n = 12
tr.shape('turtle')


for i in range(0,n):
    tr.forward(50)
    tr.stamp()
    tr.backward(50)
    tr.left(360/n)