# ===================================FUNCTIONS=================================== #

def fn():
    print('Hello Py')

fn()

# ======================================ARGUMENTS====================================== #

def fn(a=0, b=0):
    print(a + b)

fn(3,4)

# ===================================KEY ARGUMENTS================================ #

def fn(a, b=0, c=0):
    print(a, b, c)

fn(2, c=5)

def fn(a, *args, **keys):
    print(a)
    print(args[2])
    print(keys)

fn(3, 2, 4, True, user='admin', db='localhost')

# DATA PROCESSING

def fn(a, *args, **keys):
    print('args: ')
    for arg in args:
        print(arg)
    print('\nkeys: ')
    for key in keys:
        print(keys[key])
    
fn(3, 2, 4, True, user='admin', db='localhost')

# ===================================RETURN================================ #

def fn(a, b):
    return a + b

r = fn(3, 4)
print(r)

def fn(a, b):
    return a + b, a * b, a ** b

r = fn(5, 4)
print(r)

# ===================================ANONYMOUS FUNCTIONS - LAMBDA================================ #

double = lambda a: a * 2
print(double(2))
print(type(double))

square = lambda a: a * a
print(square(3))

# ===================================SCOPE - RANGE (LIFE) OF VARIABLES================================ #

# x = 1

# def fn():
#     x = 2
#     print(x)

# fn()
# print(x)

x = 1
def fn():
    global x
    x = 2
    print(x)

fn()
print(x)