#dictionary
# -a collection of key/value pairs
# -mmutable (changeable) - keys are immutable
# -indexed (by keys)
# -no duplicates
# -unordered

#--initializing dictionaries
s = {
    "a": 10, 
    "b": 20, 
    "c": 30
}
s = dict([('a',10), ("b", 20), ("c", 30)]) #just another way
s = dict(a=10, b=20, c=30) #just another way
print(s) #just prints the above dictionary object
print(len(s)) #no. of items in dictionary - 3
print(s['b']) #displays the value of 'b' - 20
print(s.get('b')) #20 - just another way
d = {'e': 40, 's': {'a': 10, "b": 20, "c": 30} }
print(len(d)) #2
print(d['e']) #40
print(d['s']) #{'a': 10, 'b': 20, 'c': 30}
print(d['s']['c']) #30

#--modifying/replacing elements
s = {'a': 10, "z": 20, "c": 30}
s["z"] = 30
print(s) #{'a': 10, 'z': 30, 'c': 30}
s["d"] = 40 #new elment added automatically, if key does not exist
print(s) #{'a': 10, 'z': 30, 'c': 30, 'd': 40}
s.pop("d") #delete an element using key
#del s["d"] #just another way
print(s) #{'a': 10, 'z': 30, 'c': 30}
#check other methods like ..
# -clear, copy, items, keys, update, values, fromkeys, setdefault, popitem etc.

#--getting keys
print("-------------just keys")
s = {'a': 10, "z": 20, "c": 30}
k = list(s)
print(k) #list of keys ['a', 'z', 'c']
k = sorted(s)
print(k) # ['a', 'c', 'z']
print("------------unpacking keys")
s = {'a': 10, "z": 20, "c": 30}
f1, f2, f3 = s #need to match the size
#f1, f2, f3 = s.keys() #just another way
print(f"f1 = {f1}, f2 = {f2}, f3 = {f3}")
print("------------unpacking values")
f1, f2, f3 = s.values() #need to match the size
print(f"f1 = {f1}, f2 = {f2}, f3 = {f3}")

#use "if" with dictionary
print("-------------------with if")
s = {'a': 10, "z": 20, "c": 30}
if "z" in s:
    print("exists")

#use "for" loop with dictionaries
print("-------------------for loop")
s = {'a': 10, "z": 20, "c": 30}
for k in s:
    print(f"{k} = {s[k]}", end = " ")
print("\n")
for k in sorted(s):
    print(f"{k} = {s[k]}", end = " ")
print("\n-------------------enumerated")
for i, k in enumerate(s):
    print(f"{i} = {k} = {s[k]}", end = ", ")
print("\n-------------------items")
for k, v in s.items():
    print(f"{k} = {v}", end = ", ")
