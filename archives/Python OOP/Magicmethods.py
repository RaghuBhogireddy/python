# Python "magic Methods"
# Customize Object behaviour and integrate with the language
# Define how objects are represented as strings
# Control access to attr vaues, both for get and set
# Build in comparision and equality testing capabilities
# Allow objects to be called like functions


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs ${self.price}/-"

    def __repr__(self):
        return f"title : {self.title}, author:{self.author}, price:{self.price}"



obj1 = Book("Ramayan", 9999,"Valmiki")
obj2 = Book("MahaBharat", 7777, "Vyasa")

print(obj1)
print(obj2)

print(str(obj2))
print(repr(obj1))