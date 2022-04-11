import sys
from random import randint
import time as t
import my_module

# =============================MODULES============================== #

# # print(sys.version)
# # print(sys.platform)
# # print(dir(sys))
# print(randint(1, 10))
# print(t.time())

msg = my_module.my_function('Dawid')
print(msg)
print('Id: ' + str(my_module.x))

# =============================ERROR HANDLING============================== #

try:
    print('try to split')
    a = 2 / 0
    print(a)
except:
    print('error!')

try:
    print('try to split')
    a = 2 / 0
    print(a)
# except TypeError:
#     print('error - wrong type of divisor')
except ZeroDivisionError:
    print('error - division by zero')

# ==================================RAISE================================== #

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('general error!')                 # error
    return a // b

try:                                                            # error handling
    r = divide(4, 0)
    print(r)
except ZeroDivisionError:                                   
    print('Cannot be divided by 0!')