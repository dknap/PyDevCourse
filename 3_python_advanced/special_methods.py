class Object:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __eq__(self, other):
        return self.value1 == other.value1 and self.value2 == other.value2

    def __str__(self):
        return f"value1: {self.value1}, value2: {self.value2}"
    
    def __repr__(self):
        text = repr(Object)
        id_obj = id(Object)
        return f"{text} {id_obj} \nvalue1: {self.value1}, value2: {self.value2}"

object1 = Object(1, 2)
object2 = Object(1, 2)

print(object1 == object2)
print(object1)
print(repr(object1))
# print(id(object1))
# print(id(object2))