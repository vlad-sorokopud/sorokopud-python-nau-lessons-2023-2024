
class LibEx(BaseException):

    def __init__(self, args):
        super().__init__(args)

    def __str__(self):
        return "LibEx"


def dickTryGetValue(dict, key):
    try:
        print("Try start")
        v = dict[key]
        print("Try end")            #
        return v
    except KeyError:
        print("Except")
        return None
    finally:
        print("End finally")


#  5000    1  351 O(N)

stud = { 15:'Sorokopud', 101:'Prystavka'}

# print(stud[15])
# print(stud[102]) -> error

# for k in stud:
#     print(f"{k} {stud[k]}")

for k, v in stud.items():
    print(f"{k} {v}")

stud[103] = 'Ivanov'

# print(stud)

studN103 = dickTryGetValue(stud, 103)
print("Student #103 " + str(studN103))
studN104 = dickTryGetValue(stud, 104)
print("Student #104 " + str(studN104))

# raise Exception("fdfdf")
raise LibEx("Invalid code")
