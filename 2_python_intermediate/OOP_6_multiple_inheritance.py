from abc import ABC, abstractmethod

class DuckBehavior(ABC):
    @abstractmethod
    def fly(self):
        print("flying..")
    
    @abstractmethod
    def say(self):
        print("kwa kwa")

    @abstractmethod
    def go_to(self):
        print("go go")

class Duck(DuckBehavior):
    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def fly(self):
        super().fly()
        
    def say(self):
        super().say()

    def go_to(self):
        super().go_to()

class Toy:

    def __init__(self, material, color):
        self.color = color
        self.material = material

class DuckToy(Toy, DuckBehavior):

    def fly(self):
        super().fly()

    def say(self):
        super().say()

    def go_to(self):
        super().go_to()

class Cat:
    def go_to(self):
        super().go_to()