import OOP_6_multiple_inheritance as Animal

duck = Animal.Duck(3, "European")
toy = Animal.DuckToy("red", "metal")
cat = Animal.Cat()

list = [duck, toy, duck, toy, cat]

for i in list:
    # if hasattr(i, "fly"):
    #     i.fly()
    try:
        i.fly()
    except AttributeError:
        print(i, "hasn't fly method")

