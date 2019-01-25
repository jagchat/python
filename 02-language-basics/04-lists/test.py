#list
# -a collection of elements/values
# -mutable (changeable)
# -allows duplicate elements
# -indexed (with an integer)
# -usually contains all elements of same type
# -guaranteed same order of elements
# -enclosed in []

#--initializing list with elements, nested lists
s = ["hello", "hai", "world", "apple", "bat", "cat"]
s = list(("hello", "hai", "world", "apple", "bat", "cat")) #just another way
print(s) #just prints the above list object
r = list(range(10,15)) #range of values converted to list
print(r) #[10, 11, 12, 13, 14]
s1 = s + ["dog", "egg"] #new list using concatenation
print(s1) #['hello', 'hai', 'world', 'apple', 'bat', 'cat', 'dog', 'egg']
print(len(s1)) #no. of elements - 8 in this case
s2 = [1, r, 4] #nested lists
print(len(s2)) #3 - no. of items
print(s2[2]) #4 - last element
print(s2[1]) #2nd element is a list -> [10, 11, 12, 13, 14]
print(s2[1][2]) #3rd element in list at 2nd list element -> [12]
s3 = [] #empty list
print(s3)

#--accessing and slicing elements
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

#list methods
s = ["hello", "hai", "world"]
s.append("a")
print(s) #['hello', 'hai', 'world', 'a']
s.insert(1, "b")
print(s) #['hello', 'b', 'hai', 'world', 'a']
#check other methods like ..
# -remove, extend, clear, pop, index, count, sort, copy, reverse

#--modifying/replacing elements
s = ["hello", "hai", "world", "apple", "bat", "cat"]
s[1] = "some" #change the 2nd element
print(s) #['hello', 'some', 'world', 'apple', 'bat', 'cat']
s[1:4] = ["a", "b", "c"] #replace elements
print(s) #["hello", "a", "b", "c", "bat", "cat"]
s[2:] = "d"
print(s) #['hello', 'a', 'd']
s[2:] = ["x", "y"]
print(s) #['hello', 'a', 'x', 'y']
print(s[-2:]) #['x', 'y']
s[-2:] = ["m", "n"]
print(s) #['hello', 'a', 'm', 'n']
s[len(s):] = ["x", "y"] #add at end
print(s) #['hello', 'a', 'm', 'n', 'x', 'y']
del s[3] #delete 3rd element
print(s) #['hello', 'a', 'm', 'x', 'y']
s[2:] = [] #remove elements from 2nd position (or use "del s[2:]")
print(s) #['hello', 'a']
s[:] = [] #remove all (or use "del s[:]")
print(s) #[]
del s #not only deletes elements but also the variable.  Cannot refer to "s" anymore
#print(s) #throws error here

#unpacking list
print("------------unpacking")
s = ["hello", "hai", "world"]
f1, f2, f3 = s #need to match the size
print(f"f1 = {f1}, f2 = {f2}, f3 = {f3}")

#use "if" with lists
print("-------------------with if")
s = ["hello", "hai", "world", "apple", "bat", "cat"]
if "hai" in s:
    print("exists")

#use "for" loop with lists
print("-------------------for loop")
s = ["hello", "hai", "world", "apple", "bat", "cat"]
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
s1 = ["hello", "hai", "world", "apple", "bat", "cat"]
s2 = [10, 20, 30, 40, 50]
for e1, e2 in zip(s1, s2):
    print(f"{e1} - {e2}", end = ", ") #shows only 5 as there are only 5 elements in s2
