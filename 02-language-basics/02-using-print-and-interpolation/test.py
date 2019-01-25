a = 10
b = 20

print(3*3) #calculated value
print("------------")
print("hello") #double quotes for string
print('hello') #same as doubel quotes
print(40 * "->") #repeats string 40 times
print("->" * 40) #just another way
print("hello" " " "world") #concats automatically (cannot be combined with variables)
print("------------")
print("a = " + str(a)) #concat strings with other typed variables
print("a = {:d}".format(a)) #using format function
print("------------")
print("hello\nWorld") #special charaters (like new line, tab etc.)
print("------------")
print("'Hello' World") #quotes inside double quotes
print("------------")
print('"Hello" World') #double quotes inside single quotes
print("------------")
print("You are\'nt doing this") #escape charaters
print("------------")
print(r"You are'nt doing this") #raw string (i.e., print as is)
print("------------")
#in the following statement "\" is optional, however new line is prevented (ignored) if we use it
print('''\
You 
are'nt 
doing 
this\
''')
print("------------")
s = "Hello World"
print("first 3 characters of '" + s + "' is '" + s[:3] + "'")
print("all characters after first 3 of '" + s + "' is '" + s[3:] + "'")
print("characters between 4 and 10 of '" + s + "' is '" + s[3:10] + "'")
print("second last character of '" + s + "' is '" + s[-2] + "'")
print("no. of characters of '" + s + "' is '" + str(len(s)) + "'")
print("------------")
print(f"Value of a = {a}") #interpolation prefix 'f'
print(f"Value of a x 10 = {a * 10}")
print("Format function: Value of a = {}, b = {}".format(a, b))
print("Format function: Value of a = {0}, b = {1}".format(a, b))
print("Format function: Value of a = {:d}, b = {:d}".format(a, b))
print("Format function: Value of a = {x}, b = {y}".format(x=a, y=b)) #named params
print("Value of a = %d" % a)
print("Value of a = %d, b = %d" % (a, b))
f = "Msg. Format: Value of a = %d, b = %d"
print(f % (a, b))
print("Another Message: %s" %s)
print("---------------")
print(s, end = ",") #equivalent to print(s + ",")
print("Value of a = %d, b = %d" % (a, b), end = ",")