#tuple
# -a collection of elements/values
# -immmutable (not changeable)
# -allows duplicate elements
# -indexed (with an integer)
# -guaranteed of same order of elements
# -enclosed in parantensis - ()

#--initializing tuple with elements, nested tuples
s = ("hello", "hai", "world", "apple", "bat", "cat")
s = "hello", "hai", "world", "apple", "bat", "cat" #just another way
s = tuple(("hello", "hai", "world", "apple", "bat", "cat")) #just another way
print(s) #just prints the above tuple object
#s = ("hi") #this is not tuple, just a string
#s = "hi" #this is not tuple, just a string
s = "hi", #note comma at end.  That makes it tuple
print(s)
s = () #empty tuple
print(s)
s1 = "hello", "hai"
print(s1[1]) #hai
s2 = "apple", "boy"
s3 = s1, s2 #nested tuple
print(s3)
print(s3[1][1]) #boy
print(len(s3)) #2

#--accessing and slicing elements
s = ("hello", "hai", "world", "apple", "bat", "cat")
print(s[1]) #prints "hai" (2nd element)
print(s[-2]) #prints "bat" (2nd from last)
s1 = s[2:] #slices from 3rd element into new list (subset)
print(s1) #['world', 'apple', 'bat', 'cat']
s1 = s[-3:] #reverse slicing
print(s1) #['apple', 'bat', 'cat']
s1 = s[:] #clone to new list
print(s1)
print(s[2]) #world
print(s[4]) #bat
s1 = s[1:4] #slice
print(s1) #["hai", "world", "apple"]

#tuple methods
s = ("1", "2", "3", "1", "4", "1", "2", "5")
print(s.count("1")) #3 - no. of "1" in tuple
print(s.index("5")) #find "5" in tuple - 7
s1 = [1, 2] #list
s2 = (1, 2, 3, 4, [1, 2], 5) #tuple with list as an element
print(s2.index(s1)) #search for list in a tuple - 4

#unpacking tuple
print("------------unpacking")
s = ("1", "2", "3")
f1, f2, f3 = s #need to match the size
print(f"f1 = {f1}, f2 = {f2}, f3 = {f3}")

#use "if" with tuples
print("-------------------with if")
s = ("hello", "hai", "world", "apple", "bat", "cat")
if "hai" in s:
    print("exists")

#use "for" loop with tuples
print("-------------------for loop")
s = ("hello", "hai", "world", "apple", "bat", "cat")
for e in s:
    print(e, end = " ")
print("\n")
for i in range(len(s)):
    print(s[i], end = " ")
print("\n-------------------sliced")
for e in s[2:]: #using slicing
    print(e, end = " ")
print("\n-------------------sorted")
for e in sorted(s):
    print(e, end = " ")
print("\n-------------------reversed")
for e in reversed(s):
    print(e, end = " ")
print("\n-------------------enumerated")
for i, e in enumerate(s):
    print(f"{i} = {e}", end = ", ")
print("\n-------------------zipped")
s1 = ("hello", "hai", "world", "apple", "bat", "cat")
s2 = (10, 20, 30, 40, 50)
for e1, e2 in zip(s1, s2):
    print(f"{e1} - {e2}", end = ", ") #shows only 5 as there are only 5 elements in s2
