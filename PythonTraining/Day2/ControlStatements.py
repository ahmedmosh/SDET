# there are three types o control statement
# 1. conditional statements: if if-else elif
# 2. looping statements: while for
# 3. jumping statements: break continue

# example : print a person is eligible for voting if age >= 18

age = 15
if age >= 18:
    print("eligible for voting")
else:
    print("abeg getout")

# Example2
if True:
    print("true condition")  # first condition will print
else:
    print("false conditions")

# example 3
if 1:
    print("one")
else:
    print("zero")

# example 3: find a number is even/odd  num%2=0
num = 10
if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

# example4: if else in single line  (ternary operator)
num = 10
print("even number") if num % 2 == 0 else print("odd number")
# example 5: multiple conditions using elif

weekNo = 5
if weekNo == 2:
    print("monday")
elif weekNo == 3:
    print("Tuesday")
elif weekNo == 4:
    print("wednesday")
else:
    print("invalid week number")

