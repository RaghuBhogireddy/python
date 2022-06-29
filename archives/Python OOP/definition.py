class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self,amount):
        self._discount = amount


obj1 = Book("Ramayan","Valmiki", 9999, 50000)
obj2 = Book("MahaBharat", "Vyasa", 7777, 45000)


print(obj1.title)
print(obj2.getprice())
obj2.setdiscount(0.25)
print(obj2.getprice())
print(obj2._discount)

