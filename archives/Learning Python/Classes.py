class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "Driving"
        self.speed = speed


class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at,", self.speed)


class MotorCycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("MotorCycle")
        if hassidecar:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my ", self.enginetype, " MotorCycle at,", self.speed)


kia = Car("gas")
tata = Car("electric")
re = MotorCycle("petrol", False)
kia.drive(240)

print(kia.wheels)
print(tata.bodystyle)
print(re.wheels)
