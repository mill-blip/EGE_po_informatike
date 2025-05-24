from itertools import *

def f(w, x, y, z):
    F = ((x <= y) or (y == w)) and ((x or z) == w)
    return F

for a in product([0, 1], repeat=4):
    table = [(1, 0, 0, 1), (0, a[0], a[1], 1), (a[2], 1, 0, a[3])]
    if len(table) == len(set(table)):
        for p in permutations('wxyz'):
            if [f(**dict(zip(p, row))) for row in table] == [1, 1, 1]:
                print(*p, sep='')