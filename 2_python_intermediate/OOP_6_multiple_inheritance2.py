import OOP_6_multiple_inheritance as Animal

myDuck = Animal.Duck(4, "African")

print("----- Live Duck -----")
myDuck.fly()
myDuck.say()
myDuck.go_to()

myToy = Animal.DuckToy("green", "aluminum")

print("----- Toy Duck -----")
myToy.fly()
myToy.say()
myToy.go_to()