#class with (instance) attributes and constructor (__init__)
class Data:

    #this method gets executed immediately when an instance is created (instantiated)
    def __init__(self):
        self.a = 0              
        self.b = 0              

    def printData(self):        #just another method
        print(f"a = {self.a}, b = {self.b}")    #can access instance attribute anywhere in class

o1 = Data()         #create instance and call constructor
o1.a = 10
o1.b = 20

o2 = Data()         #create another instance and call constructor
o2.a = 30
o2.b = 40

o1.printData() #a = 10, b = 20
o2.printData() #a = 30, b = 40
