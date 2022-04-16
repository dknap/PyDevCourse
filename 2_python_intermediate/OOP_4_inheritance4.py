from OOP_4_inheritance3 import *

n_square = Square(10)
n_rectangle = Rectangle(10, 20)

dictionary = {
            "square":n_square,
            "rectangle":n_rectangle
            }

for key, figure in dictionary.items():
    print(f"Area ({key}): ", figure.area())
    print(f"Circuit ({key}): ", figure.perimeter())
    