from datetime import date

'''
 classes
    constructor
    self
    field
    method
    access levels
        public                  dop
        private                 __dop
        protected               _dop
'''


class Book:

    def __init__(self, title: str, dop: date, publish_place: str = None):             # constructor
        self.title = title

        if type(dop) != date:
            raise Exception("Argument \'dop\' must be a \'date\' type.")

        self.__dop = dop

        # self.publish_place = publish_place
        # if self.publish_place is None:
        #     self.publish_place = '-'
        self.publish_place = publish_place if publish_place is not None else "-"

        print("LOGGER: Book was created")

    def calculate_book_age(self) -> int:
        return date.today().year - self.__dop.year

    def __str__(self) -> str:                   # c# ToString()
        return f"Book [{self.__dop},{self.title} |Publish:{self.publish_place}]"


def a():
    return "Some text"


if __name__ == "__main__":
    print("Demo using of library")

    b1 = Book("Book #1", date(2010, 4, 5))

    # .................

    b1.calculate_book_age = a
    # b1.title = "New Book# 3"
    b1.author = "Sorokopud"
    b1._Book__dop = "2000-01-27"
    # b1 = Book("book #2", "2000-01-27")

    # .................

    b2 = Book("Book #1", date(2017, 1, 18))

    # print(f"{b1} author: {b1.author} hase age: {b1.calculate_book_age()}")
    # print(f"{b2} author: {b2.author} hase age: {b2.calculate_book_age()}")

    a = b1.__dict__
    print(f"{b1} hase age: {b1.calculate_book_age()}")
