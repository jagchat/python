filename = input("Enter file name:")
f = None #mainly required here as it is going to be used out "try" scope (in "finally")
try: #watch for any errors/exceptions
    f = open(filename, "r+")
    c = f.read()
    print(c)
except FileNotFoundError: #check if this is the error
    print(f"Unable to find file: {filename}")
except OSError: #check if this is the error
    print(f"Cannot open file: {filename}")
except IOError: #check if this is the error
    print(f"Unable to read file: {filename}")
except: #some other error
    print(f"Unknown error working with: {filename}")
    #raise Exception('Cannot work with file' + filename) #re-raising error to OS
finally: #execute this regardless of whether the "try" block is successful
    if f != None and (not f.closed):
        f.close()