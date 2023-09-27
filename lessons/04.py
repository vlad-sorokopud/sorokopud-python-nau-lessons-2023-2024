import math
from typing import Tuple


def show_hi():
    print("System: Hi!!!")

    print("System: Hi2!!!!")


def add_number(a: int, b: int) -> int:
    # print(f"a({a}) + b({b}) = {a + b}")
    return a + b


def do_pow(a: int, p: int = 2):
    return a ** p


# def fig_calculation(a: float, b: float) -> Tuple[float, float]:
def fig_calculation(a, b):
    p = a + b
    s = a * b
    return p, s


def strange_function(a, b, c):
    # a*x^2 + b*2 + c = 0
    if a == 0 and b == 0 and c == 0:
        return "Not expr"

    d = b**2 - 4*a*c
    return d


# using function as a variable
# external_name = show_hi
# external_name()

# check is function change external variables
# n1 = 3
# n2 = 7
# print("n1: " + str(n1))
# print("n2: " + str(n2))
# add_number(n1, n2)
# print("n1: " + str(n1))
# print("n2: " + str(n2))

print(f"3 + 7 = {add_number(3, 7)}")
# print(add_number(3, False))     # -> 3
# print(add_number(3, "Vlad"))    # -> error

print(do_pow(6))
print(do_pow(6, 3))

fig_p, fig_s = fig_calculation(10, 15)
print(fig_s)

d = strange_function(2, 3, 1)
# d = strange_function(0, 0, 0) -> error
if d > 0:
    print("Have roots")
else:
    print("No roots")
