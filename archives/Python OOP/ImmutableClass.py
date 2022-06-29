
from dataclasses import dataclass

@dataclass(frozen=True)
class Immutable:
    value1 : str = "Immutable"
    value2 : int = 0

    def change_attr(self, new_val):
      #  self.value1 = new_val => Thows compilation error as even methods can't change the attr
        pass

obj = Immutable()
# obj.value1 = "muutable" => Even this will get Compilation  error as we can't change the class with @dataclass(frozen=True)
