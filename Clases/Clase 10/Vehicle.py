class Vehicle:
    def __init__(self,color,wheels):
        self.color = color
        self.wheels = wheels
    def describe(self):
        return f"{self.color} / {self.wheels}"

class Car(Vehicle):
    def __init__(self,color, wheels, speed, displacement):
        Vehicle.__init__(self,color,wheels)
        self.speed = speed
        self.displacement = displacement
    def describe(self):
        return f"{self.color} / {self.wheels} / {self.speed} / {self.displacement}"

class Truck(Car(Vehicle)):
    def __init__(self,color, wheels, speed, displacement, load):
        super(Car).__init__(self,color,wheels, speed, displacement)
        self.load = load
    def describe(self):
        return f"{self.color} / {self.wheels} / {self.speed} / {self.displacement} / {self.load}"

class Bicycle(Vehicle):
    def __init__(self,color,wheels,type):
        Vehicle.__init__(self,color,wheels)
        self.type = type
    def describe(self):
        return f"{self.color} / {self.wheels} / {self.type}"

class Motorcycle(Bicycle(Vehicle)):
    def __init__(self, color, wheels, type, speed, displacement):
        super(Bicycle).__init__(self, color, wheels, type)
        self.speed = speed
        self.displacement = displacement
    def describe(self):
        return f"{self.color} / {self.wheels} / {self.type} / {self.speed} / {self.displacement}"