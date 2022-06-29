

class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price

        self.author =author

        self.chapters = []

    def addchapters(self, chapter):
        self.chapters.append(chapter)

    def getpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.count
        return result

class Chapter:
    def __init__(self, name, count):
        self.name = name
        self.count = count


class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


########### We can decompose into simpler Objects using composition ##########
auth = Author("Valmiki", "Adikavi" )
book = Book("Rmayan", 999, auth )

book.addchapters(Chapter("Bala kaanda", 345))
book.addchapters(Chapter("yuddha kaanda", 567))

print(book.title)
print(book.author)
print(book.getpagecount())
