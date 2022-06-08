# Python helps us to format values of different data types in one meaningful statement
# using % or {} operators

name = "john"
age = 30
sal = 5000.50

print("The name is :", name)
print("The age is :", age)
print("The salary is :", sal)

print("name is:%s age is:%d salary is:%g" % (name, age, sal))

print("name is:{} age is:{} salary is:{}" .format(name, age, sal))
