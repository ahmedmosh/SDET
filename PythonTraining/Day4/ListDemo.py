# Example: how to create List

myList1 = [10, 20, 30, 5, 34.5]  # strings can accept integer values alone
myList2 = ["apple", "banana", "cherry", "lemon", "orange", "grape"]  # List can contain only string values
myList3 = ["apple", 10, "bread", 50]  # List can contain both integer and string values
myList4 = list()  # Empty list

print(myList1)
print(myList2)
print(myList3)
print(myList4)

# Example2 Accessing items from the list using the index number
print(myList2[2])  # prints 30
print(myList3[-2])
print(myList1[-1])
print(myList1[0])

# Example3 : range of indexes
print(myList2[1:5])
print(myList2[-4:-1])

# Example 4 : To change the item values in a list
myList2[1] = "mango"
print(myList2)  # banana has been replaced with mango in the myList2 Variable

# Example 5 :  To read list items using loop statement

for i in myList2:
    print(i)

# Example 6: To check if an item exist in a list or not
if "apple" in myList2:
    print("it is present")
else:
    print("not present")

# Example 7: To count number of items in the  list using len function
print(len(myList2))

# Example 8: To add an item to an existing list using the append or insert function in python

myList2.append("agbalumo")
print(myList2)  # added agbalumo to the end of the list
# insert is used to place an item at a particular index of a list
myList2.insert(0, "pear")
print(myList2)

# example 9: to remove item from a list using;
# pop()
myList2.pop(1)
print(myList2)
# del
del myList2[2]
print(myList2)

# clear
# myList2.clear()  # this clears the entire list item leaving the variable empty [  ]
# print(myList2)

# Example 10 : to copy list into another list using list function
myList = list(myList2)
print(myList2)
print(myList)

# copy
myList = myList2.copy()
print(myList)

# Example 11 : join/combine two lists
# using plus operator
list1 = ["a", "c", "b"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # joins list1 and list2 in a single

# using loop statement
# for i in list1:
#     list2.append(i)
# print(list2)

# using extend function
list1.extend(list2)
print(list1)
