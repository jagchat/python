#basic class with no members

class Data: #class name is "Data"
    pass    #no code (or members) as part of this class

o1 = Data() #create instance (or out object) of class "Data"
o1.a = 10   #provide some data to that (specific) instance (using attribute/field/property "a")

o2 = Data() 
o2.a = 20   #this is specific to o2 and will not have any affect on o1

print(o1.a) #shows 10
print(o2.a) #shows 20
