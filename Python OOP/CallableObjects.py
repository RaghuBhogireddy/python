class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.author = author
        self.price = price

    def __call__(self,title, price, author):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs ${self.price}/-"

obj1 = Book("Ramayan", 9999,"Valmiki")
obj2 = Book("MahaBharat", 7777, "Vyasa")

print(obj1)
obj1("Raamayan", 234324, "Adikavi Valmiki")
print(obj1)