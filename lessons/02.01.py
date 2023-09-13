# range

print(f"range(3): {range(3)}")
print(f"range(1,4): {range(1,4)}")
print(f"range(1,4,2): {range(1,4,2)}")

# loops
print("-" * 50)

print("Loop #1, i = [0, 5)")
for i in range(5):
    print(f"--- iteration {i}")

print("Loop #2, i = [1, 7)")
for i in range(1, 7):
    print(f"--- iteration {i}")

print("Loop #3, i = [0, 10) with step 3")
for i in range(0, 10, 3):
    print(f"--- iteration {i}")

print("-" * 50)

# number = int(input("Enter number:"))
number = 5
n = 0

while n != number:
    print(f"Iteration:{n+1} Count to number.")

    n += 1

print(f"Your number - {n}")

print("-" * 50)

print("Simple numbers:")
for i in range(1, 15):
    # if 1 <= i <= 2:
    if i == 1 or i == 2:
        print(f"Number {i} is simple")
        continue

    isSimple = True

    print(f"Check number: {i} div numbers: [ ", end="")
    for j in range(2, i):
        isDivided = i % j == 0
        print(f"{j}:{isDivided} ", end="")

        # if not isSimple:
        #     continue

        if isDivided:
            isSimple = False
            break

    print("]")

    # if isSimple:
    #     print(f"Number {i} is simple")
    # else:
    #     print(f"Number {i} is not simple")

    print(f"Number {i} is " + ("simple" if isSimple else "not simple"))
