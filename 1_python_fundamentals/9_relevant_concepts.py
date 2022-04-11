# =============================VALUES, OBJECTS, AND VARIABLES============================== #

a = 1
b = a
print(type(a))
print(id(a), id(b))

a = 1 
print(id(a))
a = 5
print(id(a))
a = 1 
print(id(a))

# =============================EVERYTHING IS AN OBJECT============================== #

a = 10
print(dir(10))                # list of properties, attributes for a given class

def fn():
    return 2

print(fn)
a = fn
print(a)

# =============================DATA MUTABILITY============================== #

# a = [1, 2]
# a[0] = 1000
# print(a)

# a = (1, 2)
# a[0] = 1000                   # tuple is the immutable set ERROR
# print(a)

# a = 'abc'
# # a[0] = 'b'                  # ERROR
# print(a)

# a = 1
# print(id(a))
# a += 1                        # it is not mutability
# print(id(a))

# my_list = [3, 4]
# my_tuple = (1, 2, my_list)
# print(my_tuple)
# my_tuple[2].append(5)
# print(my_tuple)

# =============================IDENTITY AND EQUALITY============================== #

a = 1
b = 1
print(a  == b)                # are they equal
print(a is b)                 # are they the same (whether it is the same object) <- two references that point to the same object

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
# print(id(a))
# print(id(b))

a = [1, 2, 3]
b = list(a)
print(a is b)                 # false - two different objects
print(a == b)                 # with equal values
print(a is not b)

# =============================FIRST CLASS FACILITY============================== #

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def apply(fn, a, b):
    return fn(a, b)

r1 = apply(add, 4, 5)
r2 = apply(multiply, 4, 5)
print(r1, r2)

# =============================DECORATORS============================== #

def my_decorator(fn):
    def wrapper():                  # The wrapper is designed to wrap around what the fn function has done
        print('Start counting')
        fn()
        print('End counting')
    return wrapper

def get_5_values():
    for v in range(1, 6):
        print(v)

# get_5_values()
get_5_values_decorated = my_decorator(get_5_values)
print(get_5_values_decorated())

# =============================DECORATORS (part 2)============================== #

def my_decorator(fn):
    def wrapper():
        print('Start counting')
        fn()
        print('End counting')
    return wrapper

@my_decorator
def get_5_values():
    for v in range(1, 6):
        print(v)

get_5_values()
# get_5_values_decorated = my_decorator(get_5_values)
# print(get_5_values_decorated())

# =============================GENERATORS============================== #

# def number_generator(end):
#     n = 1
#     while n < end:
#         yield n
#         n += 1

# values = number_generator(1000000)
# print(next(values))
# print('coś innego')
# print(next(values))
# print(next(values))

############################
#### Count to 1 000 000 ####
##########EXERCISE##########
############################

def account(goal):
    n = 1
    while n < goal:
        yield n
        n += 1
    
money = account(1000000)
while True:
    deposit = int(input('Deposit: '))
    if(deposit == 0):
        break
    while deposit > 0:
        print(next(money))
        deposit -= 1


############################
############################
############################