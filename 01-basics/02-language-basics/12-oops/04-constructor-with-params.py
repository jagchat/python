#constructor parameters

class Data:

    #this method gets executed immediately when an instance is created (instantiated)
    def __init__(self, x, y):
        self.a = x              
        self.b = y              

    def printData(self):        #just another method
        print(f"a = {self.a}, b = {self.b}")    #can access instance attribute anywhere in class

#o1 = Data()         #throws error (no parameters)
o1 = Data(10, 20)   #create instance and call constructor
o2 = Data(30, 40)   #create another instance and class constructor

o1.printData() #a = 10, b = 20
o2.printData() #a = 30, b = 40
