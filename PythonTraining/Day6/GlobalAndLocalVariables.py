# Example 1 :
global_var = 20


def func():
    local_var = 20
    print(local_var)
    print(global_var)


func()

# print(local_var)  # throws error because local_var is local variable(i.e only accessible in the function)
print(global_var)  # accessible because global_var is a global variable and can be accessed anywere

# Example 2 :  dealing with local and global variables
xy = 200  # global variable


def cool():
    xy = 100  # local variable
    print(xy)  # prints local variable


cool()  # prints local variable only

# Example 3 : updating a global variable in function
ab = 200


def update():
    global ab  # introduces the global variable into the function
    ab = 500
    print(ab)  # prints 500


update()
print(ab)  # prints 500 because ab has been updated through the function

# Example 4 :
pi = 100


def hot():
    global pi
    pi = 400
    print(pi)


hot()

# Example 4 : global variables can also be created inside a function


def sweet():
    global x
    x = 100
    print(x)


sweet()
print(x)  # the variable can also be accessed outside the function because it is variable

