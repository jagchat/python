#set
# -a collection of elements/values
# -immmutable (not changeable)
# -unindexed (cannot access using index)
# -no duplicate elements
# -unordered
# -can work with set operators (union, intersect etc.)
# -enclosed in {}

#--initializing set with elements
s = {"hello", "hai", "world", "apple", "bat", "cat"}
s = set(("hello", "hai", "world", "apple", "bat", "cat")) #just another way
print(s) #just prints the above tuple object
s = set() #empty set - cannot use s={}, it is for dictionary
print(s)
print(len(s)) #0 - no elements
s = {"hello"} #set with one element
print(s)
s = set(("hello")) #set of individual characters (unordered and non-repeated)
s = set("hello") #same as above
print(s) #{'o', 'l', 'e', 'h'}

#set operations
s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {2, 4, 6, 10}
print(s1 | s2) #{1, 2, 3, 4, 5, 6, 7, 10}
print(s1 & s2) #{2, 4, 6}
print(s1 - s2) #{1, 3, 5, 7}
print(s2 - s1) #{10}
print(s2 ^ s1) #{1, 3, 5, 7, 10}

#set methods
s = {"hello", "hai", "world"}
s.add("last")
print(s) #{'world', 'hello', 'last', 'hai'}
#check other methods like ..
# -discard, clear, copy, difference, pop, union, update, intersection, issubset, etc

#unpacking tuple
print("------------unpacking")
s = {"hello", "hai", "world"}
f1, f2, f3 = s #need to match the size
print(f"f1 = {f1}, f2 = {f2}, f3 = {f3}")

#use "if" with set
print("-------------------with if")
s = {"hello", "hai", "world", "apple", "bat", "cat"}
if "hai" in s:
    print("exists")

#use "for" loop with set
print("-------------------for loop")
s = {"hello", "hai", "world", "apple", "bat", "cat"}
for e in s:
    print(e, end = " ")
print("\n-------------------sorted")
for e in sorted(s):
    print(e, end = " ")
print("\n-------------------enumerated")
for i, e in enumerate(s):
    print(f"{i} = {e}", end = ", ")
print("\n-------------------zipped")
s1 = {"hello", "hai", "world", "apple", "bat", "cat"}
s2 = {10, 20, 30, 40, 50}
for e1, e2 in zip(s1, s2):
    print(f"{e1} - {e2}", end = ", ") #shows only 5 as there are only 5 elements in s2