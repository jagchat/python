# 'w+' - open in read/write mode, create if not exists, truncates file if exists
f = open("temp.txt", "w+") 
for x in range(1, 11):
    f.write('{0:2d} {1:3d} {2:4d}\n'.format(x, x*x, x*x*x)) #write directly to file
f.close() #close the file
print("done writing!")

print("--------------just another way")
#with automatically closes file when done with its block
with open("temp.txt", 'w+') as f1:
    for x in range(1, 11):
        f1.write('{0:2d} {1:3d} {2:4d}\n'.format(x, x*x, x*x*x)) #write directly to file
print("done writing!")
