class Numbers:

    myNumbers = 10

    def __init__(self, numbers = []):
        self.numbers = numbers


    def sumNumbers(self):
        summary = 0
        for x in self.numbers:
            summary += x
        return summary

    def multiNumbers(self):
        result = 1
        for x in self.numbers:
            result *= x
        return result

    def addNumber(self, number):
        self.numbers.append(number)

    @staticmethod
    def subtractNumber(a, b):
        return a - b

    @classmethod
    def printInformation(cls):
        print("class method")
        print("for:", cls.__name__)
        cls.myNumbers += 1

class Animal:
    howManyAnimals = 0

    @classmethod
    def __init__(cls, self, name_animal):
        self.name_animal = name_animal
        cls.howManyAnimals += 1