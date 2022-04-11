# comparing 2 objects (2nd file)

from OOP_3_objects_comparing import Person

Person1 = Person("Dawid", "Knap", "knap.dawid@outlook.com", "dknap")
Person1.printPersonInformation()
print('')
Person2 = Person("Dawid", "Knap", "knap.dawid@outlook.com", "dknap")
Person2.printPersonInformation()

print('')
print(Person1 == Person2)

print('')
print(Person1)
print(Person2)