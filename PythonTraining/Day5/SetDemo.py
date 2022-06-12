# sets are mutable objects i.e they can be modified
# Example 1 : creating set
mySet = {"apple", "banana", "cherry"}
print(mySet)  # {'banana', 'apple', 'cherry'}
# set is an unordered list/collection
# Example2 : accessing the items from set
for i in mySet:
    print(i)

# Example 2 : Value exists in set or not
print("apple" in mySet)  # boolean value

# Example 3 : adding Items to set using add(), update()

mySet.add("mango")  # add() adds singular item
print(mySet)
mySet.update(["guava", "corn"])
print(mySet)

# Example 5 : To find the number of items in a set
print(len(mySet))

# Example 6 : To remove item in sets using remove() discard()
mySet.remove("cherry")
print(mySet)

# Example 7 : to clear all items from set using the clear() function
mySet.clear()  # clears the item in a set
print(mySet)
del mySet  # this deletes the variable totally
# print(mySet)  # Throws an error cus set variable is no longer in existence

# Example 8 : joining 2 sets using Union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# update()
set3.update([8, 10, 11])

