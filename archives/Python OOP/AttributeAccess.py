class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, costs ${self.price}/-"

    def __getattribute__(self, item):
        if item == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        if key == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be float")
        return super().__setattr__(key,value)

    def __getattr__(self, item):
        return item + "is not here"



obj1 = Book("Ramayan", float(9999),"Valmiki")
obj2 = Book("MahaBharat", float(23432), "Vyasa")
obj3 = Book("Ramayan", float(2344),"Valmiki")
obj4 = Book("Bhagavatam", float(2343), "Vyasa")

obj1.price = float(9999)
print(obj1)