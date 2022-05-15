import copy

class MyClass:
    def __init__(self):
        self.a = 0

object = MyClass()
new_object = copy.copy(object)

def example(x):
    if x > 0:
        return True
    elif x < 0:
        return False
    else:
        pass

a = example(3)
b = example(-3)
c = example(0)

print(f"a:{a}, b:{b}, c:{c}")