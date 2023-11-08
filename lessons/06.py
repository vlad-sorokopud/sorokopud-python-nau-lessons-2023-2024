

class Rectangle:

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

        self._calculate_metrics()

    # @property
    # def p(self):
    #     return 2*self.__a+2*self.__b
    #
    # @property
    # def s(self):
    #     return self.__a*self.__b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, x):
        self.__a = x
        # self._calculate_metrics()

    def _calculate_metrics(self):
        self.p = 2 * self.__a + 2 * self.__b
        self.s = self.__a * self.__b

    def __str__(self):
        return f"Rectangle [a:{self.__a},b:{self.__b}] P:{self.p} S:{self.s}"


if __name__ == "__main__":
    r1 = Rectangle(2, 5)
    print(r1)
    # print(r1.a)
    r1.a = 3
    print(r1)
