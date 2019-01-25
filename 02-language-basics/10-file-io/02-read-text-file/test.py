# 'r+' - open in read/write mode 

print("--------------fetch all at once (as single text)")
f = open("temp.txt", "r+") 
c = f.read() #reads entire content of the file and places in a variable 'c' (in-memory)
f.close() #close the file
print(c)

print("--------------just another way")
#with automatically closes file when done with its block
with open("temp.txt", 'r+') as f1:
    c = f1.read()
print(c)

print("--------------fetch all at once (in the form of multiple lines)")
with open("temp.txt", "r+") as f2:
    lines = f2.readlines() #read all content
for l in lines: #going through lines after file is closed
    print(l, end = "")

print("--------------fetch line by line (for loop)")
with open("temp.txt", "r+") as f3:
    for l in f3: #read content line by line (while file is open)
        print(l, end = "")

#just another easier way
print("--------------using while loop")
with open("temp.txt", "r+") as f4:
    while True:
        l = f4.readline()
        if l == "": #if nothing returned after reading line, exit the loop
            break
        print(l, end="")