#class with instance-level attributes
class Data:

    #this is a method (method is a function in a class)
    #the first arg of every method in a class needs to be "self"
    #"self" represents current instance (context)
    def setData(self, x, y):    
        self.a = x              #"a" is an instance attribute
        self.b = y              #"b" is another instance attribute

    def printData(self):        #just another method
        print(f"a = {self.a}, b = {self.b}")    #can access instance attribute anywhere in class

o1 = Data()         #create instance
o1.setData(10,20)   #set instance data (will not affect any other instance)

o2 = Data()         #create another instance
o2.setData(30,40)   #set instance data (will not affect any other instance)

o1.printData() #a = 10, b = 20
o2.printData() #a = 30, b = 40

#can access instance attributes outside class using instance variable
print(f"o1.a = {o1.a}, b = {o1.b}")
print(f"o2.a = {o2.a}, b = {o2.b}")
