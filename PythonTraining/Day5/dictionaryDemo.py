# a dictionary is a collection which is unordered, changeable(mutable) and indexed
# in python dictionaries are written with curly brackets, and they have keys and values.
# Example 1: creating dictionary
myDic = {101: "x", 102: "y", 103: "z"}
print(myDic)

# Example2 : To access items from a dictionary
myDic1 = {
    "brand": "Hyudai",
    "model": "i10",
    "year": 2021
}
print(myDic1["brand"])
print(myDic1["model"])

# using get()
print(myDic1.get("brand"))

# Example 3 : To change values in dictionary
print(myDic1)
myDic1["year"] = 2022
print(myDic1)

# Example 4 : to read items from dictionary using loop
for i in myDic1:
    print(i)  # prints only keys from the dictionary

for i in myDic1:
    print(myDic1[i])  # prints only values from the dictionary
# OR
for i in myDic1.values():
    print(i)

for x, y in myDic1.items():
    print(x, y)

# Example 5 : to check if key exists in dictionary or not
if "model" in myDic1:
    print("exist")
else:
    print("not exist")
# OR
print("model" in myDic1)

# Example 6: to find the number of items in dictionary
print(len(myDic1))
# Example 7 : to add items to dictionary
myDic1["color"] = "red"
print(myDic1)

# Remove item from dictionary
# pop
myDic1.pop("color")  # removes color and its value fromt he dictioanry
print(myDic1)

# del
del myDic1["year"]  # removes year from the dictionary
print(myDic1)
myDic1.clear()  # clears the dictionary elements
del myDic1  # deletes the dictionary completely
