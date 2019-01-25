#in order to just check all the list of functions available in a module
#>python
#>>>import calcmodule
#>>>dir(calcmodule)
#>>>exit()

#in order to import/execute a module, we can follow any of the following

print('----------------------')
#import the module and execute functions in it
import calcmodule
sumResult = calcmodule.sum(10,20) #need to refer modulename with the function
print(f"Sum = {sumResult}")
print(f"Multipled = {calcmodule.multiply(10,20)}")

#import the module with an alias
print('----------------------')
import calcmodule as calc
sumResult = calc.sum(10,20) #need to refer alias with the function
print(f"Sum = {sumResult}")
print(f"Multipled = {calc.multiply(10,20)}")

print('----------------------')
#import individual functions directly from a module (and even aliased)
from calcmodule import sum, multiply as m
#from calcmodule import * #use this to import all functions individually (instead of naming each one)
print(f"Sum = {sum(10,20)}") #don't need to refer modulename as import it directly
print(f"Multipled = {m(10,20)}")
