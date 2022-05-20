add = lambda a,b: a+b
print(add(30, 30))

list = [add(x, y) for x,y in ([20, 20], [40, 40])]
print(list)

def make_incrementor(n):
    return lambda x: x+n

add200 = make_incrementor(200)
print(add200(50))

# sorting

square = sorted(range(-5, 13), key = lambda x: x**2)
print(square)