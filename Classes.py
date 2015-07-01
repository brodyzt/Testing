__author__ = 'brodyzt'

class Car:
    def __init__(self):
        self.color = None

    def printColor(self):
        print(self.color)


myCar = Car()
myCar.color = "Red"
myCar.printColor()