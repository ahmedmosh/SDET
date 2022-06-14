# Functions when declaring them can collect arguments
# there two types of arguments a function can collect
# positional parameters(it assigns inputed values based on the position of the arguments) and keyword parameters

# Example1:
def func(i, j):
    print(i, j)


func(10, 20)  # Positional arguments
func(j=20, i=10)  # keyword arguments

# Example 2: Default values assigned to position arguments


def func1(a, b=10):
    print(a, b)


func1(20, 100)  # value of b in the function declaration got updated upon calling the function
func1(20)  # passes the "a" parameter and gives the default parameter for b as decalred in the function declaration.

# Example 3 :
def greetings(name,greetmsg):
    print(greetmsg + " "+name)


greetings(greetmsg ="good morning", name="gold")  # keyword parameters. This can be jumbled.

# Example 4:


def myfunc(a, b, c):
    print(a, b, c)


myfunc(10, 20, 30)   # positional parameters
myfunc(a=10, b=30, c=30)  # keyword arguments
myfunc(10, 20, c=30)  # Combination of keyword and positional argument
# myfunc(10, b=20, 30)  # Throw error because positional argument must appear before keyword arguments
# Example 5 :


def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


print(largest(400, 600))


