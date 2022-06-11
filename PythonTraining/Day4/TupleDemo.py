# Tuples are also a collections characteristics like lists. but they are immutable i.e they are static in bahaviour
# Example1: creating Tuple
myTuple = ("apple", "banana", "cherry")
print(myTuple)

# Example 2: to access tuple items
print(myTuple[1])  # prints banana
print(myTuple[-1])  # prints cherry

# Example 2 : range of indexes in a tuple
myTuple1 = (1, 2, 3, 4, 5, 6, 7)
print(myTuple1[2:5])
print(myTuple1[-4:-1])

# Example 4: changing tuple objects are not possible because it is immutable
# by default for immutable variables such as tuple:
# we cannot modify existing value
# we cannot append new value
# we cannot insert a new value
# qwe cannot remove a value
# to modify a tuple you need to first convert it to a list den reconvert to a tuple?
mylist = list(myTuple1)  # converted to a list
myTuple1 = tuple(mylist)  # converted back to tuple after modification.
