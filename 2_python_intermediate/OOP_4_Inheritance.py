class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_information(self):
        print(self.name)
        print(self.age)

    def give_voice(self):
        print("Voice")
        # raise NotImplementedError()

class Mammal(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
    
    def go_to(self):
        print("go go go")
    
    def print_information(self):
        Animal.print_information(self)
        print("I'm a mammal")

class Boy(Mammal):
    
    def __init__(self, name, age, surname):
        Mammal.__init__(self, name, age)
        self.surname = surname

    def give_voice(self):
        print("Little Boy wants to play")

    def print_information(self):
        Mammal.print_information(self)
        print(self.surname)
        print("I'm a little boy")