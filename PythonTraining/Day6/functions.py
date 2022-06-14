# function are set of statements which will perform a task.
# Example
def myfun():  # function declaration
    print('hello')  # function definition


myfun()  # Calling the function


# Example 2: Functions can also take parameters or argument
def myfun1(name):
    print("hello", name)


myfun1("john")


# Example3 : to create function with multiple argument
def cal(a, b):
    return a + b


sum = cal(20, 30)
print(sum)
# OR
print(cal(10, 40))


# Example 4 :
def fun2():
    return


print(fun2())


# Example 5 :
def fun3():
    i = 10  # function will have an empty Value beacuse it is not rturning anything


print(fun3())

# Example 6 :
def calc(a,b):
    print(a + b)


calc(40, 30)
