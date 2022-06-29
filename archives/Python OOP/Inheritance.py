
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title,price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title,price)
        self.author = author
        self.pages = pages


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)




book = Book("Ramayan", "Valmiki", 9999, 9999)
nyt = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
mag = Magazine("Scientic american", "Spring Nature", 5.99, "Monthly")


print(book.author)
print(mag.publisher)
print(nyt.period)