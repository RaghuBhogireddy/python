
from abc import ABC,abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class GraphicsShape(ABC):
    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicsShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * self.radius

    def toJSON(self):
        return f"{{\"circle\" : {str(self.calcArea())} }}"



class Square(GraphicsShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side



c = Circle(23)
s = Square(25)

print(c.calcArea())
print(c.toJSON())
