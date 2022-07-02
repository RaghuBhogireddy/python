class Car:
    def __init__(self,engine,wheels,model,manufacturer):
        self.engine = engine
        self.wheels = wheels
        self.model = model
        self.manufacturer = manufacturer

    def get_engine(self):
        return self.engine

    def get_wheels(self):
        return self.wheels

    def get_model(self):
        return self.model

    def get_manufacturer(self):
        return self.manufacturer

    def display_car(self):
        return f' manufacturer : {self.get_manufacturer()}, model : {self.get_model()}, engine : {self.get_engine()}, wheels : {self.wheels}'


bmw = Car('Bs6', '4', 'SUV', 'BMW')
print(bmw.display_car())