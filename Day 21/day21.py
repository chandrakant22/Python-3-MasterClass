#Abstraction in Python

class SmartCar:
    def autoDriver(self):
        pass

    def smartAI(self):
        pass

class Audi(SmartCar):
    def autoDriver(self):
        print("Audi Smart Car Running Automatic")
    
    def smartAI(self):
        print("Audi HAve omi Smart AI")


class Bmw(SmartCar):
    def autoDriver(self):
        print("BMW Smart Car Running Automatic with 4 wheel Drive")
    
    def smartAI(self):
        print("BMW HAve roni Smart AI")

    def smartCCTV(self):
        print("BMW have BMW CCTV camera")
    


sl100=Audi()
sl100.smartAI()
sl100.autoDriver()

b400=Bmw()

b400.autoDriver()
b400.smartAI()
b400.smartCCTV()