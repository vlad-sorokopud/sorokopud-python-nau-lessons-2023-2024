print("My first python application")

v1 = 1
v2 = 1.2
v3 = "Text"
v4 = 's'
v5 = False

print("Variables module:")

'''
    Multy row comment
'''
# Row comment

# print("v1:", v1, "(", type(v1), ")")
# print("v1:" + str(v1) + " (" + str(type(v1)) + ")")
# print(f"v1:{v1} ({type(v1)})")
# print("v1:{0} ({1})".format(v1, type(v1)))

print(f"v1:{v1} ({type(v1)})")
print(f"v2:{v2} ({type(v2)})")
print(f"v3:{v3} ({type(v3)})")
print(f"v4:{v4} ({type(v4)})")
print(f"v5:{v5} ({type(v5)})")

v1 = "Vlad"

print(f"v1:{v1} ({type(v1)})")

print("Operations module:")

a = 5
b = 2

print(f"a({a}) + b({b}) = {a + b}")
print(f"a({a}) - b({b}) = {a - b}")
print(f"a({a}) * b({b}) = {a * b}")
print(f"a({a}) / b({b}) = {a / b}")
print(f"a({a}) ** b({b}) = {a ** b}")
print(f"a({a}) % b({b}) = {a % b}")
print(f"a({a}) // b({b}) = {a // b}")

print("Vlad" + " Sorokopud")
print("Vlad" * 5)

c = 1
c += b  # c = c + b

print("IfElse module:")

print(f"2 == 4 = {2 == 4}")
print(f"2 != 4 = {2 != 4}")
print(f"2 > 4 = {2 > 4}")
print(f"2 < 4 = {2 < 4}")
print(f"2 >= 4 = {2 >= 4}")
print(f"2 <= 4 = {2 <= 4}")

print("--------------------------")

# int(str) - throw ex when not number

s = input("Enter your age:")
if not s.isnumeric():
    print("It`s not a number")
    print("Ha ha")
    print("Try again")
else:
    age = int(s)

    if age < 0 or age > 120:
        print("It`s a fake age")
    elif age < 18:
        print("Not adult")
    else:
        print("Adult")


# 0 < age < 18  -> age > 0 and age < 18