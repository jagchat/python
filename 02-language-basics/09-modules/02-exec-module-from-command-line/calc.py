#in order to execute this script, use the following command at command line
#>python calc.py 10 20

#in order to execute module as a script from command line:
# -introduce a root function (named as "main" in this case)
# -put in "if" condition for "__main__" at the bottom, and execute the "main"
# -the module can still contain other functions, 
#      but have to be called either directly/indirectly from the root function



#function main (called from "if" condtion at the bottom)
def main(a, b):
    print(f"Sum = {a + b}")
    multiply(a, b)
    
#function multiply (just other functions as part of our login)
def multiply(a, b):
    print(f"Multiply = {a * b}")

#this part is executed automatically by Python run-time when working from command line
if __name__ == "__main__":
    import sys
    main(int(sys.argv[1]), int(sys.argv[2])) #call our function here