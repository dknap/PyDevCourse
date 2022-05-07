from tokenize import Number
from decorators import Numbers
from decorators import Animal

n_list = Numbers()
n_list.addNumber(3)
n_list.addNumber(5)
n_list.addNumber(6)
n_list.addNumber(7)
n_list.addNumber(8)
n_list.addNumber(13)
n_list.addNumber(2)

print(n_list.sumNumbers())
print(n_list.multiNumbers())
print(Numbers.subtractNumber(15, 5))


print(n_list.myNumbers)
print(Numbers.myNumbers)

print("Changed by classmethod:")
Numbers.printInformation()

print(n_list.myNumbers)
print(Numbers.myNumbers)

cat1 = Animal(Animal,"John")
cat2 = Animal(Animal,"John")
cat3 = Animal(Animal,"John")
cat4 = Animal(Animal,"John")
cat5 = Animal(Animal,"John")

print(cat1.howManyAnimals)