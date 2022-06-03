# Variables
# a variable is nothing but a reserved memory location to store values
# variables are used to store the data.
# Memory allocated when the values are stored in variables
# Every variable must have some type

x = 100  # integer variable data type
y = 2.00  # float variables data type
s = "welcome"  # string variables data types
print(x + y)

# variables are containers for collecting data of different types
a = 10  # integer
b = 20.5  # float

#  example 2
# : variables can be used to represent the value it contains.
print(a)
print(b)
# OR
print(a, b)


# example 3
# variables can also be declared in a single line.
d, e, f = 30, 40.5, "welcome"
print(a)
print(b)
print(f)
# OR
print(a, b, f)

# example 4
# variables can share same values i.e in python it is possible to assign the sam
# value to different varibles at one in a single line

g = h = i = 100
print(g, h, i)

# example 5
# in python programming it is possible to swap/interchange variable values between varibles
x = 1
y = 2
print(x, y)  # prints 1 2
print(y, x)  # prints 2 1
# however
x, y = y, x
print(x, y)  # prints 2 1

#  example 6
# when dealing with variables, python sees only the updated value of
# earlier stated variable(s)

q = 100
print(q)  # prints 100
# but when
q = "welcome"
print(q)  # prints welcome not the former
