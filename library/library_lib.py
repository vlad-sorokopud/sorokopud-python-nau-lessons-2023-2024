from uuid import UUID, uuid4
from datetime import date, datetime

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


class Entity:

    def __init__(self, entity_id: str = None):
        if entity_id is None:
            self._entity_id = f'{type(self).__name__}@{str(uuid4())}'
        else:
            self._entity_id = entity_id


class Book(Entity):

    def __init__(self, title: str, dop: date, entity_id: str = None, publish_place: str = None):  # constructor
        super().__init__(entity_id)  # <- call parent constructor

        self.title = title

        if type(dop) != date:
            raise Exception("Argument \'dop\' must be a \'date\' type.")

        self.__dop = dop

        # self.publish_place = publish_place
        # if self.publish_place is None:
        #     self.publish_place = '-'
        self.publish_place = publish_place if publish_place is not None else "-"

    def calculate_book_age(self) -> int:
        return date.today().year - self.__dop.year

    def to_csv_str(self) -> str:
        return f"{self._entity_id},{self.__dop},{self.title},{self.publish_place}"

    def __str__(self) -> str:                   # c# ToString()
        return f"{self._entity_id} [{self.__dop} {self.title}|Publish:{self.publish_place}]"

    @staticmethod
    def from_csv_str(data: str):
        v = data.split(',')
        if len(v) != 4:
            raise Exception("Invalid input string. CSV string must contain 4 parts.")

        return Book(v[2], datetime.strptime(v[1], '%Y-%m-%d').date(), entity_id=v[0], publish_place=v[3])


class Reader(Entity):

    def __init__(self, fio: str, dob: date, entity_id: str = None):  # constructor
        super().__init__(entity_id)  # <- call parent constructor

        self.fio = fio

        if type(dob) != date:
            raise Exception("Argument \'dob\' must be a \'date\' type.")

        self.dob = dob

    def to_csv_str(self) -> str:
        return f"{self._entity_id},{self.fio},{self.dob}"

    def __str__(self) -> str:                   # c# ToString()
        return f"{self._entity_id} [{self.fio} {self.dob}]"

    @staticmethod
    def from_csv_str(data: str):
        v = data.split(',')
        if len(v) != 3:
            raise Exception("Invalid input string. CSV string must contain 3 parts.")

        return Reader(v[1], datetime.strptime(v[2], '%Y-%m-%d').date(), entity_id=v[0])


class Library:

    def __init__(self):
        self.__books = []
        self.__readers = []
        pass

    # ---------- Add methods ---------------------------------------------------------------------------------------- #

    def add_book(self, book: Book):
        self.__books.append(book)

    def add_reader(self, reader: Reader):
        self.__readers.append(reader)

    # ---------- Show methods --------------------------------------------------------------------------------------- #

    def show_books(self):
        print(f"Library books ({len(self.__books)}):")
        for idx, book in enumerate(self.__books):
            print(f"\t #{idx} {book}")

    def show_readers(self):
        print(f"Library readers ({len(self.__readers)}):")
        for idx, reader in enumerate(self.__readers):
            print(f"\t #{idx} {reader}")

    # ---------- Data methods --------------------------------------------------------------------------------------- #

    @staticmethod
    def load_from(path):
        library = Library()

        with open(path, 'r') as f:
            fl = f.readline()[:-1]
            # counts_str = fl.split(',')
            # if len(counts_str) != 2:
            #     raise Exception("First line in file, must contain 2 value")
            #
            # book_count = int(counts_str[0])
            # readers_count = int(counts_str[1])

            counts = [int(x) for x in fl.split(',')]
            if len(counts) != 2:
                raise Exception("First line in file, must contain 2 value")

            for i in range(counts[0]):
                line = f.readline()[:-1]
                library.__books.append(Book.from_csv_str(line))
            for i in range(counts[1]):
                line = f.readline()[:-1]
                library.__readers.append(Reader.from_csv_str(line))

        return library

    def save_to(self, path):
        # file work op# 1
        # f = open(path, 'x')
        # ...
        # f.close()

        with open(path, 'w+') as f:
            f.write(f"{len(self.__books)},{len(self.__readers)}")
            for b in self.__books:
                f.write(f"\n{b.to_csv_str()}")
            for r in self.__readers:
                f.write(f"\n{r.to_csv_str()}")


if __name__ == "__main__":
    print("Demo using of library")

    b1 = Book.from_csv_str("Book@d2a4ace7-4672-4e0b-b397-322f11e3d840,1997-06-26,Harry Potter and the Philosopher's Stone,United Kingdom");
    # b1 = Book("Book #1", date(2010, 4, 5))
    print(b1)
    # .................

    # b1.calculate_book_age = a
    # b1.title = "New Book# 3"
    # b1.author = "Sorokopud"
    # b1._Book__dop = "2000-01-27"
    # b1 = Book("book #2", "2000-01-27")

    # .................

    # b2 = Book("Book #1", date(2017, 1, 18))

    # print(f"{b1} author: {b1.author} hase age: {b1.calculate_book_age()}")
    # print(f"{b2} author: {b2.author} hase age: {b2.calculate_book_age()}")

    # a = b1.__dict__
    # print(f"{b1} hase age: {b1.calculate_book_age()}")

    # e1 = Entity()
    # print(e1._entity_id)
