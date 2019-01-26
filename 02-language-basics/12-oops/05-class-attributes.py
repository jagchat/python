#class with class-level attributes
class Data:

    s = 100 #class-level attribute, shared across all instances

    def __init__(self, x):    
        self.a = x              #instance-level attribute

    def printData(self):        #just another method
        print(f"s = {self.s}, a = {self.a}")    #can access instance/class attribute anywhere in class

print(f"Data.s = {Data.s}") #can be accessed directly - Data.s = 100

o1 = Data(10)
o2 = Data(20)

o1.printData() #s = 100, a = 10
o2.printData() #s = 100, a = 20

#can access class/instance attributes outside class using instance variable
print(f"o1.s = {o1.s}, a = {o1.a}") #o1.s = 100, a = 10
print(f"o2.s = {o2.s}, a = {o2.a}") #o2.s = 100, a = 20

Data.s = 200 #affects in every instance
o1.printData() #s = 200, a = 10
o2.printData() #s = 200, a = 20
print(f"Data.s = {Data.s}") #Data.s = 200

#BEWARE
o1.s = 1000 #creates new instance attribute inside 'o1' (does not modify Data.s)
o1.printData() #s = 1000, a = 10
print(f"Data.s = {Data.s}") #Data.s = 200