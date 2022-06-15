# approach 1
import animal
import bird

animal.fly()
animal.color()
bird.fly()
bird.color()

# Approach 2
from animal import *
fly()
color()  # best practice for this approach is to call the functions immediately after importing else latest import
# will override especially when they share the same function.
from bird import *
fly()
color()