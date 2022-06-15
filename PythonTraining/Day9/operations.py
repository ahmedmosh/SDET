# Approach 1
import calculator  # imports a module

calculator.add(100, 200)
calculator.mul(5, 20)

# Approach 2
from calculator import add, mul  # to import specific functions from a module
add(40, 20)
mul(20,5)

# Approach 3
from calculator import *  # This imports all the functions and method in a module
add()
mul()