# Create a string variables
# when creating a string variable you introduce the quotation

# Ways of creating a string variable
# s = "welcome"
# s = 'welcome'
# s = str("welcome")
#
# # creating empty variables
# name = str()
# name = ""
# name = ''

# Strings are immutable
# Mutable-cannot change the value of the variable
# Immutable-can change the value of the variable

str1 = "welcome"
print(id(str1))

str1 = str1 + "to python"
print(id(str1))

# + and * with strings
str2 = "welcome"
print(str2 + "programming")  # concatenating/joining
print(str2 * 2)

# slicing

str3 = "welcome"
print(str3[1:3])  # el
print(str3[:6])  # welcom
print(str3[2:])  # lcome
print(str3[1:-1])

# ord() and chr() to print ASCII characters
print(ord("A"))  # 65
print(chr(65))

# max() min() len()
print(max("abc"))  # c
print(min("abc"))  # a
print(len("abc"))  # 3

# "in" and "not in" operators this returns boolean values
# s = "welcome"
# print("com" in s)
# print("lome" not in s)

# string comparism
# print("tim" == "tie")  # false
# print("tim" != "tie")
# print("tim" <= "tie")
# print("tim" >= "tie")
# print("" == "tie")

# string testing

x = "welcome"
print(x.isalnum())
print(x.isdigit())
print(x.islower())
print(x.isupper())

# searching for substrings
v = "welcome to python"
print(v.endswith("thon"))  # True
print(v.startswith("good"))  # false
print(v.find("come"))  # 3
print(v.count("o"))  # returns number of occurrence

# converting strings
h = "string in python"
h1 = h.capitalize()
print(h1)  # String in python

h2 = h.title()
print(h2)  # String In Python

h3 = h.upper()
print(h3)  # STRING IN PYTHON

h4 = h.replace("i", "o")
print(h4)
