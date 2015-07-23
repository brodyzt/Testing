'''__author__ = 'brodyzt'

class Car:
    def __init__(self):
        self.color = None

    def printColor(self):
        print(self.color)


myCar = Car()
myCar.color = "Red"
myCar.printColor()'''

class Test:
    def __init__(self):
        self.structure = [1,2,3,4,5]

    def __iter__(self):
        return self.structure

mine = Test()
print()