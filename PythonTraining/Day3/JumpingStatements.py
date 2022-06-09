# jumping statements are mostly used with conditional statements and looping statements
# They include "break" and "continue"
# As soon as condition is met the execution jumps to next level

# ____ break as a jumping statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print("program exited!!!")  # upon reaching 5, for block will stop

# ____ continue as a jumping statement
for x in range(1, 10):
    if x == 5:
        continue
    print(x)
print("program exited!!!")  # upon reaching 5, for block will skip
