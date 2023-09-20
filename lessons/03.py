import random

l1 = [1, "Vlad", 6, 4.5, "Sorokopud"]

print(f"l1 : {l1}, type: {type(l1)}, len: {len(l1)}")

print(f"-------LIST: l1 -----------------------------------")
for i in range(len(l1)):
    print(f"--- --- l1[{i}] = {l1[i]}")

# for i in range(1, 6):
#     i *= -1
#     print(f"--- --- l1[{i}] = {l1[i]}")

print(f"-------LIST: l1 -----------------------------------")
for el in l1:
    print(f"--- --- {el}")

print(f"-------LIST: l1 -----------------------------------")
for i, el in enumerate(l1):
    print(f"--- --- l1[{i}] = {el}")

print(f"------- Indexes -----------------------------------")
print(l1[2])
print(l1[-2])
print(l1[2:])   # take all elements from index 2
print(l1[:3])   # take all elements from start to index 3
print(l1[2:4])  # take from index 2 to index 4

print(f"------- List actions -----------------------------------")

l1.append(615)          # add element to list (from end)
l1.extend([6, -15])     # add a collection of elements to list (from end)
# l1.clear()
l1.insert(2, "Text")    # add element to list, on specific index
# l1.remove(6)            # remove element from array, by value, only 1 element
l1.index(6)             # return a index of element, if not exist throw error
l1.count(6)             # return a count of elements
# l1.sort()
# l1.reverse()
# l1.pop(1)             # remove element from array by index

# while l1.count(6) > 0:
#     l1.remove(6)

print(f"-------LIST: l1 -----------------------------------")
for i in range(len(l1)):
    print(f"--- --- l1[{i}] = {l1[i]}")

print(f"-----------------------------------------")
l2 = [[1, 2], [3, 4], [5, 6]]
l3 = [[1, 2], [3, 4, 5], [5, 6, 7, 8]]

# print(len(l2))
# print(len(l3))

for i in range(len(l2)):
    for j in range(len(l2[i])):
        print(f"{l2[i][j]} ", end="")
    print("")

print("_________________________________________")

for i in range(len(l3)):
    for j in range(len(l3[i])):
        print(f"{l3[i][j]} ", end="")
    print("")

print(f"--------- LIST GENERATORS --------------------------------")
# l4 = [x for x in range(10)]
# l4 = [random.randint(-100, 100) for x in range(15)]
# l4 = [x for x in range(10) if x % 2 != 0]
# l4 = [x**2 for x in range(10)]

l4 = [[random.random() for x in range(3)] for y in range(3)]
for i in range(len(l4)):
    for j in range(len(l4[i])):
        print(f"{l4[i][j]} ", end="")
    print("")

# print(l4)