import math                                       # import math in file (op#1)
# from math import *                              # import math in file (op#2) NOT RECOMENDED
# from math import pow, ceil, floor, sqrt         # import math in file (op#3)
import random

print(pow(5, -1))

print(math.ceil(1.45), math.ceil(1.75))
print(math.floor(1.45), math.floor(1.75))

print(math.sqrt(9))

print(random.randint(1, 150))
print(random.random())              # float 0 - 1
print(random.random()*5 + 5)        # float 5 - 10

print(random.choice([1, 3, 7, 8]))
