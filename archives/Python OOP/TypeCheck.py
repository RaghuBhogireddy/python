class Book:
    def __init__(self, title):
        self.title = title

class NewsPaper:
    def __init__(self, name):
        self.name = name


book = Book("Ramayan")
book2 = Book("Mahabharat")
newspaper = NewsPaper("Times of India")



print(type(book) == type(newspaper))
print(type(book) == type(book2))

# Instead of using type() check, we can use isinstace(object, class)

print(isinstance(book,Book))
print(isinstance(book,object))