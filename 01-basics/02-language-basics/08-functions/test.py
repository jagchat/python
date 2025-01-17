print("-----simple function")
def f1(): #define a function "f1" with no params/args
    #body of function
    #write as many lines as you want
    print("in f1")
f1() #execute function

print("-----with args")
def f2(a, b): #define a function accepting two args
    print(f"a = {a}, b = {b}, sum = {a+b}")
f2(10,20) #execute function

print("-----return result")
def f3(a, b): 
    return a+b #return the value from function
r = f3(10,20) #execute function and catch the returned result
print(f"Sum = {r}")

print("-----with args defaults")
def f4(a=10, b=20): #define a function accepting two args
    print(f"a = {a}, b = {b}, sum = {a+b}")
f4() #a = 10, b = 20, sum = 30
f4(40) #a = 40, b = 20, sum = 60
f4(50,30) #a = 50, b = 30, sum = 80
f4(b=50) #named argument - a = 10, b = 50, sum = 60

print("-----persistance of function arg")
#the default values are evaluated only once (not during every call)
#objects like lists etc., maintain their previous values
def f5(a=10, l=[]): 
    l.append(a)
    print(l)
    return l #just in case
f5() #[10]
f5(20) #[10, 20]
f5(30) #[10, 20, 30]

print("-----if not to persist function arg")
def f6(a=10, l=None): 
    if l is None:
        l = []
    l.append(a)
    print(l)
f6() #[10]
f6(20) #[20]
f6(30) #[30]

print("---dynamic args")
def f7(a, *args):
    print(f"a={a}")    
    for arg in args:
        print(arg)
f7(1,2,3,4) #displays "a=1" and all rest of the values (2,3,4)

print("---dynamic args with additional args")
def f8(a, *args, s):
    print(f"a={a}")    
    for arg in args:
        print(arg, end=s)
f8(1,2,3,4, s="|")  #displays "a=1" and all rest of the values "2|3|4"

print("---dynamic args with arg names")
def f9(a, **args):
    print(f"a={a}")    
    for n in args:
        print(f"{n}={args[n]}")
f9(10, b=20, c=30) #displays "a=10" and finally "b=20","c=30"    
#f9(1,2,3,4) #error as no arg names provided

print("---dynamic args/keywords")
def f10(a, *args, **keywords):
    print(f"a={a}")    
    for arg in args:
        print(arg)
    for k in keywords:
        print(f"{k}={keywords[k]}")
f10(1,2,3,4) #displays "a=1" and all rest of the values
f10(10,40,50, b=20, c=30) #displays "a=10", and then "40", "50" and finally "b=20","c=30"
#f10(10,b=20, c=30, 40,50) #error - order messed up
f10(10, b=20, c=30) #fine "a=10", "b=20", "c=30"

print("---unpacking list")
def f11(a,b):
    print(f"a = {a}, b = {b}")
l = [10,20]
f11(*l) #a = 10, b = 20
print("---unpacking tuple")
l = (10,20)
f11(*l) #a = 10, b = 20
print("---unpacking set")
l = {10,20}
f11(*l) #a = 10, b = 20
print("---unpacking dictionary")
l = {'a':10, 'b':20}
f11(*l) #a = a, b = b
f11(**l) #a = 10, b = 20