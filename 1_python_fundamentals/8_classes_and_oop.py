# # ==================================CREATE AN EMPTY CLASS=============================== #

class Point:
    pass

p1 = Point()
p2 = Point()
print(p1)
print(type(p1))

# # ===================================INITIALIZER / METHODS================================ #

class Point:
    def __init__(self, x=0, y=0):             # basic initializer
        self.x = x
        self.y = y

    def move_to_new_coords(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point(3, 5)
print('Default points:', p1.x, ',', p1.y)
p1.move_to_new_coords(12, 4)
print('New points:', p1.x, ',', p1.y)

# # ====================================CLASS ATTRIBUTES===================================== #

class Point:
    points_counter = 0
    def __init__(self, x=0, y=0):               # basic initializer
        self.x = x
        self.y = y
        Point.points_counter += 1

    def move_to_new_coords(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point(3, 5)
p2 = Point(4, 9)
# p2.points_counter = 12
# Point.points_counter = 2
# print(p2.points_counter)
# print(Point.points_counter)
print(Point.points_counter)

# # =========================================INHERITANCE===================================== #

class Widget:
    def __init__(self, label):
        self.label = label

w = Widget('my widget')
print(w.label)
class Button(Widget):                   # the Button class extends from the Widget class
    def __init__(self, label, size):
        super().__init__(label)
        self.size = size

    def handle_click(self):
        return 'Click!'

b = Button('my button', 'large')
print(b.label, b.size)
print(b.handle_click())