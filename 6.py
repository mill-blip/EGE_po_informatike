import turtle as t
t.left(90)
l = 20
t.begin_fill()
for i in range(7):
    t.forward(10 * l)
    t.right(120)
t.end_fill()
count = 0
canvas = t.getcanvas()
for x in range(-100*l, 100*l, l):
    for y in range(-100*l, 100*l, l):
        z = canvas.find_overlapping(x, y, x, y)
        if len(z) == 1 and z[0] == 5:
            count += 1
print(count)
t.update()