# fields

class Car:
    def __init__(self, model, brand, vinnumber):
        self.model = model
        self.brand = brand
        self.vinnumber = vinnumber
    
    def printInformation(self):
        print("My model is: ", self.model)
        print("My car brand is ", self.brand)
        print("My car vinnumber: ", self.vinnumber)

myCar1 = Car('126p', 'Fiat', 'Gh6756hGHgghj87656')
myCar2 = Car('125p', 'Fiat', 'GHTH66765446456532')

myCar1.printInformation()
print('')
myCar2.printInformation()