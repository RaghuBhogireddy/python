class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, other):
        if not isinstance(other,Book):
            raise ValueError("Couldn't compare book to non-book")
        return (self.title == other.title and
                self.price == other.price and
                self.author == other.author)

    def __ge__(self, other):
        if not isinstance(other,Book):
            raise ValueError("Couldn't compare book to non-book")
        return self.price >= other.price

    def __lt__(self, other):
        if not isinstance(other,Book):
            raise ValueError("Couldn't compare book to non-book")
        return self.price < other.price


obj1 = Book("Ramayan", 9999,"Valmiki")
obj2 = Book("MahaBharat", 7777, "Vyasa")
obj3 = Book("Ramayan", 9999,"Valmiki")
obj4 = Book("Bhagavatam", 5789, "Vyasa")

print(obj1==obj3)
print(obj1 >= obj2)
print(obj1 < obj2)
books = [obj4,obj3,obj2,obj1]
books.sort()
print([book.title for book in books])