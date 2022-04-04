
from abc import ABC,abstractmethod

class GraphicsShape(ABC):
    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicsShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * self.radius



class Square(GraphicsShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side



c = Circle(23)
s = Square(25)

print(c.calcArea())
print(s.calcArea())