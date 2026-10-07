class Car:
    def __init__(self, acc, brk, clutch):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started....")

car1 = Car(True, False, True)
car1.start(True, False, True)