
from dataclasses import dataclass, field
import random

def pages_func():
    return random.randrange(450,800)

@dataclass
class Book:
    # we can add default values to attr when declared,
    # default value attr are always declared at last
    # instead of assigning value, we can use "field(default=value)"
    # We can use default_factory instead of default such that it will call a function to assign value
    title : str
    author : str
    price : float
    pages : int = field(default_factory=pages_func)

## Additional Object Initalization can be done using __post_init__ method, since __init__ doesn't exist
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, that has {self.pages} pages"


obj1 = Book("Ramayan","Valmiki", 2434234)
obj2 = Book("MahaBharat","Vyasa", 234234)

print(obj2.price)

# dataclasses automatically takes care of __rper__, __str__ & __eq__
# We can use user provided methods as usual
print(repr(obj2))
print(obj2 == obj1)
print(obj2.description)

print(obj2)
print(obj1)