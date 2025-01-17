a = 10
b = 20

##taking input from user (uncomment following)
#a = int(input("Enter first no:"))
#b = int(input("Enter second no:"))

print("--------------")
print("Sum = " + str(a+b))

print("------if condition--------")
if a is b: #or we can also write a==b
    #can have multiple lines here
    print("Yes. Both are same")
elif a > b:
    print("{:d} is greater than {:d}".format(a, b))
else:
    print("{:d} is greater than {:d}".format(b, a))

if a > 5 and b > 5:
    print("Both are above 5")

print("------for loop (0 to 4)--------")
s = ""
for i in range(5):
    #"break" and "continue" would work similar to other lang.
    s += str(i) + ","
print(s)

print("------for loop (10 to 14)--------")
s = ""
for i in range(10, 15):
    s += str(i) + ","
print(s)

print("------for loop (10 to 20 using step)--------")
s = ""
for i in range(10, 20, 2): #step 2
    print(str(i), end = ",")

print("\n------while loop--------")
i = 1
s = ""
while i < 10:
    print(str(i), end = ",")
    i += 1
print("\n")

