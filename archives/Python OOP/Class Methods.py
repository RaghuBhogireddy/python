# instances methods works on sepcific objects
# class methods works on entire class
# static methods won't modify state of either class or specific class instance

class Book:

    BOOK_TYPES=("HAND COVER", "PAPER BACK", "HARD COPY")

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    __booklist = None

    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    def __init__(self,title,booktype):
        self.title = title
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} is not a valid book type")
        else: self.booktype = booktype

    def setTitle(self,title):
        self.title = title

print("booktypes:", Book.getbooktypes())

b1 = Book("Ramayan", "PAPER BACK")
b2 = Book("mahaBharat", "PAPER BACK")
books = Book.getbooklist()
books.append(b1)
books.append(b2)
print(books)



