# hermetization (2nd file)

from OOP_2_hermetization import Car
value = float(input('Provide the amount of fluids: '))
unit = input(' L for liters, G for gallons: ')

myCar = Car()
myCar.setTank(value, unit)

while True:
    choice = int(input('[0] - liters to gallons [1] - change tank size [2] - exit: '))
    if choice == 2:
        break
    elif choice == 0:
        unit = input('L for liters, G for gallons: ')
        print(myCar.getTank(unit))
    elif choice == 1:
        value = float(input('Provide the amount of fluids: '))
        unit = input('L for liters, G for gallons: ')
        myCar.setTank(value, unit)
    else:
        pass