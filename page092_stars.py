import turtle as t

size = 300
points = 11
angle = 180 - (180 / points)

t.color('red')
t.begin_fill()
for i in range(points):
    t.forward(size)
    t.right(angle)

t.end_fill()