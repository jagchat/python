#package => module which is namespaced for structural hierarchy
# -prevents collisions of same function names across multiple modules
# -in order to create packages, 
# --create respective folder hierararchy (package/subpackage/nested)
# --place "__init__.py" in each of those folders (automatically turns them to packages)
# --just code your modules just the way as you want in those folders

#import a package/subpackage and execute a function
import jag.utils
jag.utils.line()

#import a package/subpackage/nested-subpackage and execute a function
import jag.lib.calc
sumResult = jag.lib.calc.sum(10,20)
print(f"Sum = {sumResult}")
multiplyResult = jag.lib.calc.multiply(10,20)
print(f"Multiplied = {multiplyResult}")

#just another way
from jag.utils import line
from jag.lib.calc import sum, multiply as m
line()
sumResult = sum(10,20)
print(f"Sum = {sumResult}")
multiplyResult = m(10,20)
print(f"Multiplied = {multiplyResult}")
