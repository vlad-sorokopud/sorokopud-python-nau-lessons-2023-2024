from datetime import date

# import library_lib                                       # op 1
import library_lib as lib                                # op 2
from library_lib import Book, Reader, Library              # op 3

#library_lib.show_library_status()                        # op 1
#lib.show_library_status()                                # op 2
#show_library_status()                                    # op 3

if __name__ == "__main__":          # if this file is main file in the project
    # library = Library()
    #
    # library.add_book(Book('Harry Potter and the Philosopher\'s Stone', date(1997, 6, 26), publish_place="United Kingdom"))
    # library.add_book(Book('Harry Potter and the Chamber of Secrets', date(1992, 6, 2)))
    #
    # library.add_reader(Reader("Sorokopud V.I", date(1996, 4, 11)))
    #
    # library.show_books()
    # library.show_readers()
    #
    # library.save_to("data.bak")

    library = Library.load_from("data.bak")
    library.show_books()
    library.show_readers()
