
class TestObj:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.next is not None:
            return self.next
        else:
            raise StopIteration

    def __str__(self):
        return f"TestObj[{self.id},{self.name}]"


if __name__ == "__main__":
    t3 = TestObj(15,'V')

    t2 = TestObj(14, "C")
    t2.next = t3

    t1 = TestObj(4,'A')
    t1.next = t2

    for el in t1:
        print(el)
