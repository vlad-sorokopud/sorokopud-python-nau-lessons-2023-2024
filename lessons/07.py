from functools import reduce

# lambda

def isGteaterThan3Func(v):
    if v > 3:
        return True
    return False

def isGteaterThan(arr, v):
    c = 0
    for i in l:
        if i > v:
            c += 1
    return c


l = [3, 5, -5, 2, 15, 17, 4, 8]

c = 0
for i in l:
    if i > 3:
        c+=1
print(f"Count of element which greater than 3: {c}")
print(f"Count of element which greater than 3: {isGteaterThan(l, 3)}")

isGreaterThen3 = lambda x: x > 3
print(isGreaterThen3(5))
print(isGreaterThen3(1))

# ll = sum([True for x in l if x > 3])
ll = sum([True for x in l if isGreaterThen3(x)])
print(ll)

# collection app_tools

## filter

# for i in filter(isGreaterThen3, l):
#     print(i)

# l2 = [x for x in filter(isGreaterThen3, l)]
# l2 = [x for x in filter(lambda v: v > 3, l)]
# l2 = list(filter(lambda v: v > 3, l))
# l2 = list(filter(isGteaterThan3Func, l))
l2 = list(filter(lambda v: v > 3, l))
# l2 = list(filter(lambda  i, v: True, l))
print(l2)

## map

# l3 = list(map(lambda a,b: a + b, [1, 2, 3], [4, 5, 6]))
l3 = list(map(lambda a,b, c: a + b + c, [1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(l3)

## reduce


pow2 = lambda x, y: x * y
p = l[0]
for i in range(1, len(l)):
    p = pow2(p, l[i])
print(p)

l4 = reduce(lambda x, y: x* y, l)
print(l4)

## zip

l5 = list(zip([1,2,3,4], [5,6,7,8]))
print(l5)
