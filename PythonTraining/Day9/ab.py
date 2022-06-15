# Approach 1:
import a
import b

anim = a.Animal()
anim.display()

bir = b.Bird()
bir.display()

# Approach 2:

from a import Animal
from b import Bird

anim1 = Animal()
anim1.display()

anim2 = Animal()
anim2.display()
